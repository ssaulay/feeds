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


REF_LABELS = {
    "quoted": "Tweet cité",
    "replied_to": "En réponse à",
    "retweeted": "Retweet de",
}


def resolve_referenced(tweet: dict) -> list[dict]:
    """Tweets cités/répondus résolus en entrées {url, content} (texte inclus dans
    la réponse bookmarks, cf. x_client). Récupère le contenu que le filtrage des
    liens x.com laissait de côté (quote tweets, fils de réponses)."""
    out = []
    for ref in tweet.get("referenced", []):
        cited = ref.get("tweet") or {}
        if not cited.get("id"):
            continue
        username = cited.get("author", {}).get("username", "inconnu")
        label = REF_LABELS.get(ref.get("type"), "Tweet lié")
        url = f"https://x.com/{username}/status/{cited['id']}"
        out.append({"url": url, "content": f"{label} @{username} : {tweet_text(cited)}"})
    return out


def resolve_tweet(tweet: dict) -> list[dict]:
    """Retourne [{url, content|None}] : tweets cités puis liens sortants du tweet."""
    referenced = resolve_referenced(tweet)
    links = [{"url": url, "content": fetch_page_content(url)} for url in extract_links(tweet)]
    return referenced + links
