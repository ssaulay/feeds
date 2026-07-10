"""Résolution des liens d'un tweet et extraction du contenu des pages liées."""

import httpx

MAX_CONTENT_CHARS = 20_000
USER_AGENT = "Mozilla/5.0 (compatible; feeds-knowledge-pipeline/1.0)"


def tweet_text(tweet: dict) -> str:
    """Texte complet du tweet (les posts longs vivent dans note_tweet)."""
    note = tweet.get("note_tweet") or {}
    return note.get("text") or tweet.get("text", "")


def extract_links(tweet: dict) -> list[str]:
    """URLs sortantes du tweet, déjà dé-t.co-ifiées par l'API (expanded_url)."""
    urls = []
    for source in (tweet.get("entities"), (tweet.get("note_tweet") or {}).get("entities")):
        for u in (source or {}).get("urls", []):
            expanded = u.get("expanded_url") or u.get("url")
            # Ignorer les liens internes X (média du tweet, quote tweets…)
            if expanded and not expanded.startswith(("https://x.com/", "https://twitter.com/")):
                urls.append(expanded)
    return list(dict.fromkeys(urls))


def fetch_page_content(url: str) -> str | None:
    """Télécharge une page et en extrait le texte principal (markdown)."""
    import trafilatura

    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30,
                         headers={"User-Agent": USER_AGENT})
        resp.raise_for_status()
    except httpx.HTTPError:
        return None
    content = trafilatura.extract(resp.text, output_format="markdown",
                                  include_links=False, url=str(resp.url))
    if not content:
        return None
    return content[:MAX_CONTENT_CHARS]


def resolve_tweet(tweet: dict) -> list[dict]:
    """Retourne [{url, content|None}] pour chaque lien sortant du tweet."""
    return [{"url": url, "content": fetch_page_content(url)} for url in extract_links(tweet)]
