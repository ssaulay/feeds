"""Smoke tests hors réseau : état, extraction (parsing), notes et index."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.config import Config
from pipeline.extract import _parse_json, _sanitize
from pipeline.notes import (generate_indexes, parse_frontmatter, rebuild_sources_section,
                            update_topic_note, write_source_note)
from pipeline.resolve import extract_links, resolve_referenced, tweet_text
from pipeline.state import load_seen_ids, save_seen_ids

TWEET = {
    "id": "1943000000000000001",
    "created_at": "2026-07-09T08:00:00.000Z",
    "text": "Great thread on prompt caching https://t.co/abc",
    "author": {"username": "someone", "name": "Some One"},
    "entities": {"urls": [
        {"url": "https://t.co/abc", "expanded_url": "https://example.com/article"},
        {"url": "https://t.co/def", "expanded_url": "https://x.com/foo/status/1"},
    ]},
}
EXTRACTION = {
    "slug": "prompt-caching-basics",
    "title": "Les bases du prompt caching",
    "summary": "Un résumé.",
    "key_ideas": ["Idée 1", "Idée 2"],
    "quotes": ["Une citation"],
    "tags": ["llm", "prompt-engineering"],
    "primary_topic": "prompt-engineering",
    "proposed_tags": [],
}
LINKS = [{"url": "https://example.com/article", "content": "Contenu archivé."}]


def tmp_config(root: Path) -> Config:
    return Config(
        repo_root=root, sources_dir=root / "sources", notes_dir=root / "notes",
        indexes_dir=root / "indexes", state_dir=root / "state",
        taxonomy_path=root / "taxonomy.yaml", token_path=root / "state" / "token.enc",
    )


class SmokeTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.cfg = tmp_config(Path(self._tmp.name))

    def tearDown(self):
        self._tmp.cleanup()

    def test_state_roundtrip(self):
        save_seen_ids(self.cfg.seen_ids_path, {"2", "1"})
        self.assertEqual(load_seen_ids(self.cfg.seen_ids_path), {"1", "2"})

    def test_resolve_helpers(self):
        self.assertEqual(tweet_text(TWEET), TWEET["text"])
        # Les liens internes X sont filtrés
        self.assertEqual(extract_links(TWEET), ["https://example.com/article"])

    def test_resolve_referenced(self):
        tweet = {
            "id": "1943000000000000002",
            "referenced": [
                {"type": "quoted", "tweet": {
                    "id": "1900000000000000000",
                    "text": "Le contenu cité important",
                    "author": {"username": "citee"}}},
                {"type": "replied_to", "tweet": {
                    "id": "1800000000000000000",
                    "note_tweet": {"text": "Le long post parent"},
                    "author": {"username": "parent"}}},
            ],
        }
        refs = resolve_referenced(tweet)
        self.assertEqual([r["url"] for r in refs], [
            "https://x.com/citee/status/1900000000000000000",
            "https://x.com/parent/status/1800000000000000000",
        ])
        self.assertIn("Tweet cité @citee : Le contenu cité important", refs[0]["content"])
        self.assertIn("En réponse à @parent : Le long post parent", refs[1]["content"])
        # Un tweet sans référence ne produit rien
        self.assertEqual(resolve_referenced({"id": "x"}), [])

    def test_extract_parse_and_sanitize(self):
        parsed = _parse_json('bla {"slug": "A B!", "tags": ["llm", "hors-taxo"],'
                             ' "primary_topic": "hors-taxo"} bla')
        clean = _sanitize(parsed, ["llm", "misc"])
        self.assertEqual(clean["tags"], ["llm"])
        self.assertEqual(clean["primary_topic"], "llm")
        self.assertEqual(clean["slug"], "a-b")

    def test_source_note_topic_note_and_indexes(self):
        path = write_source_note(self.cfg, TWEET, TWEET["text"], LINKS, EXTRACTION)
        self.assertEqual(path.name, "1943000000000000001-prompt-caching-basics.md")
        self.assertIn("/2026/", str(path))
        content = path.read_text()
        self.assertIn("## Archive du contenu lié", content)
        self.assertIn("Contenu archivé.", content)

        fm = parse_frontmatter(path)
        self.assertEqual(fm["tweet_id"], TWEET["id"])
        self.assertEqual(fm["primary_topic"], "prompt-engineering")

        # Première occurrence du thème : création sans appel LLM
        note_path = update_topic_note(self.cfg, EXTRACTION, path)
        note = note_path.read_text()
        self.assertIn("# prompt-engineering", note)
        self.assertIn("../sources/2026/1943000000000000001-prompt-caching-basics.md", note)

        # La section Sources est reconstruite par code : une liste tronquée
        # (ou réécrite par le LLM) est restaurée depuis le frontmatter des sources.
        note_path.write_text(note.split("## Sources")[0] + "## Sources\n\n(vidé)\n")
        rebuild_sources_section(self.cfg, "prompt-engineering")
        restored = note_path.read_text()
        self.assertNotIn("(vidé)", restored)
        self.assertIn("../sources/2026/1943000000000000001-prompt-caching-basics.md", restored)
        self.assertEqual(restored.count("## Sources"), 1)

        generate_indexes(self.cfg)
        by_tag = (self.cfg.indexes_dir / "by-tag.md").read_text()
        self.assertIn("## prompt-engineering", by_tag)
        by_date = (self.cfg.indexes_dir / "by-date.md").read_text()
        self.assertIn("2026-07-09", by_date)


if __name__ == "__main__":
    unittest.main()
