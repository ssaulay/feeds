# feeds — bookmarks X → bibliothèque de savoir personnelle

## Le projet

Pipeline quotidien : récupérer les bookmarks X de Simon (quelques posts/jour),
lire leur contenu et les pages liées, en extraire du savoir via Claude, et le
consolider dans une bibliothèque markdown versionnée dans ce repo.

Documents de référence :
- `docs/reco-pinned-tweets-knowledge.md` — design complet, décisions et justifications
- `README.md` — mise en route et fonctionnement

## Décisions structurantes (ne pas re-débattre sans raison)

- **API X directe** (pay-per-use, endpoint bookmarks = "owned reads" $0.001/post)
  pour le pipeline automatique ; le MCP X hébergé (`api.x.com/mcp`) est réservé à
  l'exploration interactive.
- **Deux couches de stockage** : `sources/` (1 note immuable par bookmark, avec
  archive du contenu lié — anti link rot) + `notes/` (synthèses par thème,
  vivantes, mises à jour par le pipeline à chaque apport). Répertoire plat,
  date en frontmatter, jamais de dossiers par thème.
- **Taxonomie contrôlée** (`taxonomy.yaml`) : l'extracteur choisit dedans ;
  les suggestions vont dans `proposed_tags` (frontmatter) et sont validées à la
  main. Ne jamais laisser le LLM créer des tags librement.
- **Markdown + git = source de vérité.** Pas de base vectorielle (grep + tags
  suffisent à ce volume) ; Notion éventuellement en miroir, jamais en source.
- **Token X** : refresh tokens rotatifs (usage unique) → token chiffré Fernet
  committé dans `state/token.enc`, recommitté par la CI à chaque refresh ; seule
  `TOKEN_ENC_KEY` est en secret GitHub. Ne jamais committer clé ou token en clair.
- **Noms de fichiers stables** (`<tweet_id>-<slug>.md`), index régénérés avec
  tri déterministe.

## État du code

**Pipeline en production depuis le 2026-07-13** : autorisé, testé en local, et
validé en CI de bout en bout (run `workflow_dispatch` → 38 notes sources + 13
notes de synthèse committées par la CI). Cron quotidienne active.

Composants (testés hors réseau via `.venv/bin/python -m unittest tests.test_smoke`) :
- `pipeline/x_client.py` — OAuth2 + refresh, fetch bookmarks (1 page de 50, dédup en aval)
- `pipeline/resolve.py` — liens sortants (expanded_url, liens X internes filtrés),
  extraction de contenu via trafilatura, cap 20k chars
- `pipeline/extract.py` — appel Claude (JSON : slug, résumé, idées clés, citations,
  tags, primary_topic), sanitization contre la taxonomie
- `pipeline/notes.py` — notes sources, notes de synthèse (création directe la
  1ère fois, mise à jour via Claude ensuite), index by-tag/by-date
- `pipeline/main.py` — orchestration (`--limit N`) ; un bookmark en échec n'est
  pas marqué vu → retenté au run suivant
- `scripts/authorize.py` — autorisation initiale OAuth 2.0 PKCE (interactif, local)
- `.github/workflows/ingest.yml` — cron quotidienne 06:17 UTC + workflow_dispatch

## Où on en est / prochaines étapes

Bootstrap terminé (app X, OAuth, secrets GitHub, CI validée — la branche
`claude/pinned-tweets-knowledge-tool-0bv44t` EST la branche par défaut). Reste :

1. ⬜ **Surveiller le 1er refresh de token en prod** : la cron de demain 06:17 UTC
   sera le premier run où l'access token a expiré → refresh + rotation +
   recommit de `state/token.enc` par la CI. Chemin pas encore exercé en réel.
   Après un run local, toujours `git pull` avant le suivant (token rotatif).
2. 🟡 **Qualité** : ✅ tweets cités/répondus désormais résolus (expansion
   `referenced_tweets.id`, contenu inclus gratis dans la réponse bookmarks —
   ~24/50 bookmarks concernés). Limite connue : un tweet cité qui n'est qu'une
   **image** n'est pas capté (pas d'OCR/vision). Reste à itérer : prompts
   d'extraction/consolidation, taxonomie à ajuster aux vrais bookmarks.
3. ✅ Notes « contenu inaccessible » d'avant le fix retraitées (2026-07-14) :
   8 notes supprimées + IDs dé-marqués de `state/seen_ids.json` → elles seront
   régénérées (avec les tweets cités résolus) au prochain run cron. `notes/misc.md`
   réécrite (ne garde que les 2 posts média-only). La note « atelier Anthropic »
   (2048418646960288059) est postérieure au fix : son quote tweet ne contient
   qu'une vidéo → non retraitée (limite média, pas de vision/OCR).

**Env local** : venv 3.12 obligatoire (`.venv/bin/python`), jamais `python3` (=3.9).

## Conventions

- Échanges et contenu de la bibliothèque en **français** ; code/identifiants en anglais.
- Documenter les décisions dans `docs/reco-pinned-tweets-knowledge.md`
  (section « Historique des décisions »).
