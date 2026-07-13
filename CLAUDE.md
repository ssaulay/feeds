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

Pipeline bootstrappé et testé hors réseau (`python -m unittest tests.test_smoke`) :
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

1. ✅ App développeur X créée (confidential, callback `http://localhost:8484/callback`)
2. ✅ Autorisation OAuth faite : `state/token.enc` écrit, `TOKEN_ENC_KEY` dans `.env`,
   appel réel `/users/me` + bookmarks validé (`@ssaulay`). **Env : venv 3.12
   obligatoire (`.venv/bin/python`), pas `python3` (=3.9, casse le code).**
3. ✅ Premier run local (`--limit 2`) : 3 notes sources + synthèse `ai-agents.md`
   produites et validées. A révélé et corrigé un bug : le modèle renvoie parfois
   un bloc *thinking* avant le texte → on cherche le bloc `type=="text"`
   (`extract.py` + `notes.py`) au lieu de `content[0].text`.
   ⬜ Reste à committer le code + les notes + `state/`.
4. ⬜ Secrets GitHub : `X_CLIENT_ID`, `X_CLIENT_SECRET` (client confidentiel),
   `TOKEN_ENC_KEY`, `ANTHROPIC_API_KEY`
5. ⬜ Merger la branche `claude/pinned-tweets-knowledge-tool-0bv44t` sur la
   branche par défaut (les crons GitHub ne tournent que dessus)
6. ⬜ Itérer sur la qualité : prompts d'extraction/consolidation, taxonomie de
   départ à ajuster aux vrais bookmarks

## Conventions

- Échanges et contenu de la bibliothèque en **français** ; code/identifiants en anglais.
- Documenter les décisions dans `docs/reco-pinned-tweets-knowledge.md`
  (section « Historique des décisions »).
