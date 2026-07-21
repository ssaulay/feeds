"""Extraction de savoir d'un bookmark via l'API Claude (sortie structurée)."""

import base64
import json
import re

from .resolve import collect_images, fetch_image

EXTRACTION_PROMPT = """\
Tu enrichis une bibliothèque de savoir personnelle à partir de posts X bookmarkés.

Voici un post bookmarké et, le cas échéant, le contenu des pages qu'il référence.

<post auteur="@{username}" date="{created_at}">
{text}
</post>

{linked_section}
{images_section}
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


def _images_section(images: list[dict]) -> str:
    """Décrit les images jointes (elles suivent en blocs image dans le message)."""
    if not images:
        return ""
    lines = []
    for img in images:
        desc = f"- image ({img['origin']}, {img['type']})"
        if img.get("alt"):
            desc += f" — texte alternatif : {img['alt']}"
        lines.append(desc)
    return ("Des images sont jointes à ce message (post et/ou tweets cités). "
            "Lis-les : exploite tout texte, schéma, graphique ou donnée qu'elles "
            "contiennent, notamment quand le post lui-même est court.\n"
            + "\n".join(lines) + "\n")


def _image_blocks(tweet: dict) -> tuple[list[dict], list[dict]]:
    """Télécharge les images du tweet ; retourne (blocs image API, métadonnées)
    pour les seules images effectivement récupérées."""
    blocks, attached = [], []
    for img in collect_images(tweet):
        fetched = fetch_image(img["url"])
        if not fetched:
            continue
        media_type, data = fetched
        blocks.append({"type": "image", "source": {
            "type": "base64", "media_type": media_type,
            "data": base64.standard_b64encode(data).decode()}})
        attached.append(img)
    return blocks, attached


def _parse_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"Pas de JSON dans la réponse du modèle : {text[:200]}")
    # strict=False : tolère les caractères de contrôle bruts (ex. retour à la
    # ligne littéral dans une chaîne) que le modèle insère parfois.
    return json.loads(match.group(0), strict=False)


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
    image_blocks, attached = _image_blocks(tweet)
    prompt = EXTRACTION_PROMPT.format(
        username=tweet.get("author", {}).get("username", "inconnu"),
        created_at=tweet.get("created_at", ""),
        text=text,
        linked_section=_linked_section(links),
        images_section=_images_section(attached),
        taxonomy="\n".join(f"- {t}" for t in taxonomy),
    )
    content = image_blocks + [{"type": "text", "text": prompt}]
    response = client.messages.create(
        model=cfg.claude_model,
        max_tokens=2000,
        messages=[{"role": "user", "content": content}],
    )
    # Le modèle peut émettre un bloc thinking avant le texte : on prend le bloc texte.
    text_out = next(
        (b.text for b in response.content if getattr(b, "type", None) == "text"), None)
    if text_out is None:
        raise ValueError("Pas de bloc texte dans la réponse du modèle")
    return _sanitize(_parse_json(text_out), taxonomy)
