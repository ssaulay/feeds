"""Écriture des notes sources (immuables), notes de synthèse (vivantes) et index."""

from datetime import datetime, timezone
from pathlib import Path

import yaml

SOURCE_TEMPLATE = """---
{frontmatter}---

# {title}

> Post de **@{username}** — [voir sur X]({tweet_url})

## Résumé

{summary}

## Idées clés

{key_ideas}
{quotes_section}
## Texte du post

{text}
{archive_section}"""

TOPIC_NOTE_TEMPLATE = """# {topic}

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

{summary}

## Sources

{sources}
"""

UPDATE_NOTE_PROMPT = """\
Tu maintiens une note de synthèse vivante sur le thème « {topic} » dans une
bibliothèque de savoir personnelle. Voici la note actuelle :

<note>
{existing}
</note>

Nouvel apport (source : {source_ref}) :

<apport>
Titre : {title}
Résumé : {summary}
Idées clés :
{key_ideas}
</apport>

Réécris la note complète en intégrant cet apport : fusionne avec l'existant,
déduplique, signale explicitement les contradictions ("⚠️ Contradiction : ...").
Garde la structure (titre, ## Synthèse, ## Sources), ajoute la ligne
"- [{title}]({source_rel_path})" à la section Sources (conserve les lignes
existantes). Reste concis : la note doit tenir sous ~150 lignes en priorisant
les idées les plus fortes. Réponds avec le markdown complet de la note, rien d'autre.
"""


def _frontmatter(data: dict) -> str:
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=True, default_flow_style=False)


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text()
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return yaml.safe_load(text[4:end])


def write_source_note(cfg, tweet: dict, text: str, links: list[dict],
                      extraction: dict) -> Path:
    created = tweet.get("created_at", "")
    year = created[:4] or str(datetime.now(timezone.utc).year)
    username = tweet.get("author", {}).get("username", "inconnu")
    tweet_url = f"https://x.com/{username}/status/{tweet['id']}"

    fm = _frontmatter({
        "tweet_id": tweet["id"],
        "author": f"@{username}",
        "date": created,
        "url": tweet_url,
        "links": [l["url"] for l in links],
        "tags": extraction["tags"],
        "primary_topic": extraction["primary_topic"],
        "proposed_tags": extraction.get("proposed_tags", []),
        "title": extraction["title"],
    })
    key_ideas = "\n".join(f"- {idea}" for idea in extraction.get("key_ideas", []))
    quotes = extraction.get("quotes", [])
    quotes_section = ""
    if quotes:
        quotes_section = "\n## Citations\n\n" + "\n".join(f"> {q}\n" for q in quotes)

    # Archive anti link rot : le texte extrait des pages liées vit dans la note.
    archived = [l for l in links if l.get("content")]
    archive_section = ""
    if archived:
        blocks = "\n\n".join(f"### {l['url']}\n\n{l['content']}" for l in archived)
        archive_section = f"\n## Archive du contenu lié\n\n{blocks}\n"

    note = SOURCE_TEMPLATE.format(
        frontmatter=fm, title=extraction["title"], username=username,
        tweet_url=tweet_url, summary=extraction["summary"], key_ideas=key_ideas,
        quotes_section=quotes_section, text=text, archive_section=archive_section,
    )
    path = cfg.sources_dir / year / f"{tweet['id']}-{extraction['slug']}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(note)
    return path


def update_topic_note(cfg, extraction: dict, source_path: Path) -> Path:
    topic = extraction["primary_topic"]
    path = cfg.notes_dir / f"{topic}.md"
    source_rel = f"../{source_path.relative_to(cfg.repo_root)}"

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(TOPIC_NOTE_TEMPLATE.format(
            topic=topic,
            summary=extraction["summary"],
            sources=f"- [{extraction['title']}]({source_rel})",
        ))
        return path

    import anthropic

    prompt = UPDATE_NOTE_PROMPT.format(
        topic=topic,
        existing=path.read_text(),
        source_ref=source_rel,
        title=extraction["title"],
        summary=extraction["summary"],
        key_ideas="\n".join(f"- {i}" for i in extraction.get("key_ideas", [])),
        source_rel_path=source_rel,
    )
    client = anthropic.Anthropic(api_key=cfg.anthropic_api_key)
    response = client.messages.create(
        model=cfg.claude_model,
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}],
    )
    # Le modèle peut émettre un bloc thinking avant le texte : on prend le bloc texte.
    text_out = next(
        (b.text for b in response.content if getattr(b, "type", None) == "text"), None)
    if text_out is None:
        raise ValueError("Pas de bloc texte dans la réponse du modèle")
    updated = text_out.strip()
    if updated.startswith("```"):
        updated = updated.strip("`").removeprefix("markdown").strip()
    path.write_text(updated + "\n")
    return path


def generate_indexes(cfg) -> None:
    """Index dérivés, régénérés avec tri déterministe (pas de bruit de diff)."""
    entries = []
    for path in sorted(cfg.sources_dir.rglob("*.md")):
        fm = parse_frontmatter(path)
        if fm:
            fm["_rel"] = f"../{path.relative_to(cfg.repo_root)}"
            entries.append(fm)
    cfg.indexes_dir.mkdir(parents=True, exist_ok=True)

    by_date = sorted(entries, key=lambda e: (e.get("date", ""), e["tweet_id"]), reverse=True)
    lines = ["# Index par date", ""]
    lines += [f"- {e.get('date', '')[:10]} — [{e['title']}]({e['_rel']}) ({e['author']})"
              for e in by_date]
    (cfg.indexes_dir / "by-date.md").write_text("\n".join(lines) + "\n")

    by_tag: dict[str, list[dict]] = {}
    for e in entries:
        for tag in e.get("tags", []):
            by_tag.setdefault(tag, []).append(e)
    lines = ["# Index par tag", ""]
    for tag in sorted(by_tag):
        lines.append(f"## {tag}")
        lines.append("")
        for e in sorted(by_tag[tag], key=lambda e: (e.get("date", ""), e["tweet_id"]),
                        reverse=True):
            lines.append(f"- [{e['title']}]({e['_rel']}) ({e['author']})")
        lines.append("")
    (cfg.indexes_dir / "by-tag.md").write_text("\n".join(lines).rstrip() + "\n")
