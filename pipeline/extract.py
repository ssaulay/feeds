"""Extraction de savoir d'un bookmark via l'API Claude (sortie structurée)."""

import json
import re

EXTRACTION_PROMPT = """\
Tu enrichis une bibliothèque de savoir personnelle à partir de posts X bookmarkés.

Voici un post bookmarké et, le cas échéant, le contenu des pages qu'il référence.

<post auteur="@{username}" date="{created_at}">
{text}
</post>

{linked_section}

Tags autorisés (vocabulaire contrôlé, choisis UNIQUEMENT dedans) :
{taxonomy}

Réponds avec un objet JSON seul (pas de markdown autour) :
{{
  "slug": "titre-court-en-kebab-case (max 6 mots, ascii)",
  "title": "Titre descriptif de l'apport de ce contenu",
  "summary": "Résumé en 2-4 phrases, en français",
  "key_ideas": ["idée clé actionnable ou insight, 1 phrase chacune", "..."],
  "quotes": ["citation marquante exacte si pertinente (sinon liste vide)"],
  "tags": ["2-4 tags choisis dans le vocabulaire autorisé"],
  "primary_topic": "le tag principal (un seul, parmi tags)",
  "proposed_tags": ["nouveau tag utile absent du vocabulaire (souvent vide)"]
}}
"""

LINKED_TEMPLATE = """<contenu_lié url="{url}">
{content}
</contenu_lié>"""


def _linked_section(links: list[dict]) -> str:
    parts = [LINKED_TEMPLATE.format(url=l["url"], content=l["content"])
             for l in links if l.get("content")]
    return "\n\n".join(parts) if parts else "(pas de lien sortant exploitable)"


def _parse_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"Pas de JSON dans la réponse du modèle : {text[:200]}")
    return json.loads(match.group(0))


def _sanitize(extraction: dict, taxonomy: list[str]) -> dict:
    tags = [t for t in extraction.get("tags", []) if t in taxonomy] or ["misc"]
    primary = extraction.get("primary_topic")
    extraction["tags"] = tags
    extraction["primary_topic"] = primary if primary in tags else tags[0]
    extraction["slug"] = re.sub(r"[^a-z0-9-]", "", str(extraction.get("slug", "sans-titre"))
                                .lower().replace(" ", "-"))[:60] or "sans-titre"
    return extraction


def extract_knowledge(cfg, tweet: dict, text: str, links: list[dict],
                      taxonomy: list[str]) -> dict:
    import anthropic

    client = anthropic.Anthropic(api_key=cfg.anthropic_api_key)
    prompt = EXTRACTION_PROMPT.format(
        username=tweet.get("author", {}).get("username", "inconnu"),
        created_at=tweet.get("created_at", ""),
        text=text,
        linked_section=_linked_section(links),
        taxonomy="\n".join(f"- {t}" for t in taxonomy),
    )
    response = client.messages.create(
        model=cfg.claude_model,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    # Le modèle peut émettre un bloc thinking avant le texte : on prend le bloc texte.
    text_out = next(
        (b.text for b in response.content if getattr(b, "type", None) == "text"), None)
    if text_out is None:
        raise ValueError("Pas de bloc texte dans la réponse du modèle")
    return _sanitize(_parse_json(text_out), taxonomy)
