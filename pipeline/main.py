"""Orchestration : fetch bookmarks → résoudre liens → extraire → notes + index.

Usage : python -m pipeline.main [--limit N] [--backfill N]
"""

import argparse
import sys

import yaml

from .config import load_config
from .notes import generate_indexes, update_topic_note, write_source_note
from .resolve import resolve_tweet, tweet_text
from .state import load_seen_ids, save_seen_ids
from .x_client import XClient


def load_taxonomy(cfg) -> list[str]:
    return yaml.safe_load(cfg.taxonomy_path.read_text())["tags"]


def run(limit: int | None = None, backfill: int | None = None) -> int:
    cfg = load_config()
    if not cfg.anthropic_api_key:
        raise SystemExit("ANTHROPIC_API_KEY manquant")
    taxonomy = load_taxonomy(cfg)
    client = XClient(cfg)

    user = client.me()
    print(f"Compte : @{user['username']} ({user['id']})")

    seen = load_seen_ids(cfg.seen_ids_path)
    if backfill:
        # Remonte l'historique page par page jusqu'à accumuler N bookmarks
        # jamais traités (ou épuiser les ~800 que conserve X).
        new, fetched = [], 0
        for page in client.iter_bookmark_pages(user["id"]):
            fetched += len(page)
            new += [t for t in page if t["id"] not in seen]
            if len(new) >= backfill:
                new = new[:backfill]
                break
        print(f"Backfill : {fetched} bookmarks parcourus, {len(new)} à traiter")
    else:
        bookmarks = client.fetch_bookmarks(user["id"])
        new = [t for t in bookmarks if t["id"] not in seen]
        print(f"{len(bookmarks)} bookmarks récupérés, {len(new)} nouveaux à traiter")
    if limit:
        new = new[:limit]

    processed = 0
    for tweet in new:
        text = tweet_text(tweet)
        print(f"→ {tweet['id']} (@{tweet.get('author', {}).get('username', '?')})")
        try:
            from .extract import extract_knowledge

            links = resolve_tweet(tweet)
            extraction = extract_knowledge(cfg, tweet, text, links, taxonomy)
            source_path = write_source_note(cfg, tweet, text, links, extraction)
            update_topic_note(cfg, extraction, source_path)
            print(f"  ✓ {source_path.relative_to(cfg.repo_root)}"
                  f" [{', '.join(extraction['tags'])}]")
        except Exception as exc:  # un bookmark en échec ne bloque pas les autres
            print(f"  ✗ échec ({exc!r}) — sera retenté au prochain run", file=sys.stderr)
            continue
        seen.add(tweet["id"])
        processed += 1
        save_seen_ids(cfg.seen_ids_path, seen)

    if processed:
        generate_indexes(cfg)
    print(f"Terminé : {processed} note(s) créée(s)")
    return processed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=None,
                        help="traiter au plus N nouveaux bookmarks")
    parser.add_argument("--backfill", type=int, default=None,
                        help="paginer au-delà de la 1re page jusqu'à N bookmarks non traités")
    args = parser.parse_args()
    run(limit=args.limit, backfill=args.backfill)


if __name__ == "__main__":
    main()
