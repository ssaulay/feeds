# Reco — Outil « bookmarks X → bibliothèque de savoir »

*Rédigé le 2026-07-10.*

## Clarification préalable

Sur X, on ne peut « épingler » qu'un seul post sur son profil. Ce que tu décris
(« quelques posts par jour ») correspond aux **bookmarks (signets)**. Tout ce qui
suit part de ce principe : le geste quotidien = bookmarker un post, et l'outil
récupère les nouveaux bookmarks.

## État des lieux API / MCP (juillet 2026)

- **Plus de free tier** : depuis février 2026, l'API X est en *pay-per-use* par
  défaut pour les nouveaux développeurs (carte bancaire requise).
- **Bookmarks = « owned reads »** : depuis le 20 avril 2026, `GET /2/users/{id}/bookmarks`
  coûte **$0.001 par post lu**. À ~5 bookmarks/jour, on parle de **moins de 1 $/mois**
  (même en relisant une fenêtre de recouvrement pour la déduplication).
- **MCP officiel hébergé** : lancé le 30 juin 2026 à `api.x.com/mcp` (~200 endpoints,
  dont les bookmarks). L'auth passe par un pont local `xurl` (`npx @xdevplatform/xurl mcp`)
  qui gère l'OAuth 2.0 et le refresh des tokens. Il consomme les **mêmes crédits API**
  — le MCP n'est pas une alternative gratuite, c'est une autre porte d'entrée.
- **Auth requise** : OAuth 2.0 *user context* avec scopes `bookmark.read`,
  `users.read`, `tweet.read`, `offline.access` (pour le refresh token).

## Recommandation

### Architecture cible : script planifié (API directe) + extraction LLM

Le MCP est excellent pour l'**exploration interactive** (poser des questions sur tes
bookmarks depuis Claude Code), mais pour un pipeline **automatique quotidien**, un
petit script est plus robuste : pas de client MCP à faire tourner, gestion d'état
explicite, exécutable en GitHub Action.

Pipeline proposé (1× par jour suffit vu le volume) :

1. **Fetch** — `GET /2/users/:id/bookmarks` (avec `expansions` pour les URLs,
   médias, threads). Déduplication via un fichier d'état (`state/seen_ids.json`)
   committé dans le repo.
2. **Résolution des liens** — suivre les `t.co`, télécharger le contenu des pages
   liées (readability → markdown). Prévoir un fallback (certains sites bloquent les bots).
3. **Extraction + consolidation** — un appel Claude API par bookmark : résumé,
   idées clés, tags (vocabulaire contrôlé), citations. Puis mise à jour des notes
   de synthèse concernées (voir structure ci-dessous).
4. **Stockage** — voir « Structure de stockage » ci-dessous.
5. **Planification** — GitHub Action cron quotidienne (ou une Routine Claude Code
   si tu veux que l'extraction soit agentique plutôt qu'un simple appel API).

### Structure de stockage (révisée après challenge)

La première version (`knowledge/YYYY/` + un fichier par bookmark + index par thème)
était une structure d'**archive**, pas de **bibliothèque** : des résumés isolés et
figés qui s'empilent sans jamais se consolider. Version retenue — deux couches,
inspirée d'un Zettelkasten simplifié :

```
sources/2026/1943012345-titre-court.md   # IMMUABLE : 1 note par bookmark
notes/prompt-engineering.md              # VIVANTE : synthèse par thème, mise à jour
taxonomy.yaml                            # vocabulaire de tags contrôlé
indexes/                                 # dérivés, régénérés (tri déterministe)
state/seen_ids.json                      # état du pipeline (déduplication)
```

Principes, avec la justification long terme :

- **Deux couches sources/notes.** `sources/` capture le fait brut (post, auteur,
  date, extraction) et n'est plus jamais modifié. `notes/` contient des notes de
  synthèse par thème que le pipeline *met à jour* à chaque nouvel apport (intégrer,
  dédupliquer, signaler les contradictions), avec liens vers les sources. C'est la
  couche qui capitalise : dix bookmarks sur un sujet → une compréhension consolidée,
  pas dix fiches redondantes.
- **Répertoire plat, date en métadonnée.** On cherche « ce que je sais sur X »,
  jamais « ce que j'ai bookmarké en 2026 ». La date vit dans le frontmatter ; les
  regroupements (par tag, par période) sont des index dérivés. Pas de dossiers par
  thème non plus : un contenu chevauche toujours deux thèmes et la taxonomie évolue.
- **Vocabulaire de tags contrôlé.** Tags libres générés par LLM = divergence garantie
  (`ia`/`AI`/`llm`/`genai` en six mois). L'extracteur choisit dans `taxonomy.yaml` ;
  les nouveaux tags sont *proposés* dans un champ séparé et validés manuellement.
- **Archivage anti link rot.** Les posts se suppriment, les articles liés
  disparaissent. Le texte extrait des liens (readability → markdown) est archivé
  dans la note source. À long terme c'est la partie la plus précieuse du repo.
- **Noms de fichiers stables** basés sur l'ID du tweet — jamais de renommage, les
  liens internes survivent. Index régénérés avec tri déterministe pour éviter le
  bruit de diff à chaque run.
- **Pas de base vectorielle pour l'instant.** À quelques posts/jour, grep + tags
  suffisent pendant des années. Un index sémantique pourra être ajouté plus tard
  comme artefact *dérivé* — jamais comme source de vérité.

Markdown + git restent la source de vérité : format le plus durable (portable,
diffable, lisible par un humain, Obsidian ou n'importe quel agent).

### Où le MCP officiel a sa place

Ajoute quand même le MCP X à ton Claude Code local : idéal pour interroger tes
bookmarks à la demande (« qu'est-ce que j'ai bookmarké sur les agents ce mois-ci ? »),
tester les endpoints, et déboguer le pipeline. Config type :

```json
{
  "mcpServers": {
    "x": {
      "command": "npx",
      "args": ["@xdevplatform/xurl", "mcp", "https://api.x.com/mcp"],
      "env": { "CLIENT_ID": "...", "CLIENT_SECRET": "..." }
    }
  }
}
```

⚠️ Ne jamais committer `~/.xurl` (cache de tokens vivants) ni les secrets de l'app.

### Variante stockage : Notion

Si tu préfères consulter la bibliothèque hors du repo, l'étape 4 peut écrire dans
une base Notion (une page par bookmark, propriétés = tags/date/source) via l'API ou
le MCP Notion. Reco : garder le markdown dans git comme source de vérité et pousser
vers Notion en miroir — ça évite de dépendre d'un seul outil.

## Historique des décisions

- **2026-07-14** — Articles X (`x.com/i/article/…`, ~9 % du corpus) : la piste
  API officielle est fermée. Les endpoints Articles de l'API v2 sont en
  **écriture seule** (`POST /2/articles/draft`, `POST /2/articles/{id}/publish`) ;
  aucun GET, et le tweet porteur ne contient qu'un lien t.co (pas de body).
  Le MCP hébergé expose les mêmes endpoints → même limite. Alternatives
  possibles, non retenues pour l'instant : rendu headless authentifié (fragile,
  session web à maintenir), API tierces de scraping (coût, ToS). Décision :
  marquer ces sources comme non récupérables et re-vérifier périodiquement si
  X ouvre la lecture (demande communautaire active — thread « CRUD Articles »).

- **2026-07-10** — Structure de stockage révisée : abandon de `knowledge/YYYY/`
  (archive chronologique) au profit du modèle deux couches `sources/` + `notes/`
  avec taxonomie contrôlée et archivage du contenu lié (voir section dédiée).

## Coûts estimés (5 bookmarks/jour)

| Poste | Estimation |
|---|---|
| API X (owned reads + marge de recouvrement) | < 1 $/mois |
| Claude API (extraction, ~1 appel Sonnet/bookmark) | ~1–3 $/mois |
| GitHub Actions (repo privé, 1 run/jour) | gratuit (quota largement suffisant) |

## Prochaines étapes proposées

1. Créer l'app développeur X (portail dev, mode pay-per-use), activer OAuth 2.0
   avec les scopes ci-dessus, récupérer client_id/secret.
2. Bootstrapper le script d'ingestion (Python ou TypeScript) : auth + fetch +
   état de déduplication.
3. Ajouter l'étape d'extraction Claude + le format de note markdown.
4. Brancher la GitHub Action cron et itérer sur la qualité des notes.

## Sources

- [X API pricing (docs officielles)](https://docs.x.com/x-api/getting-started/pricing)
- [Annonce pricing « Owned Reads » $0.001 — 20 avril 2026](https://devcommunity.x.com/t/x-api-pricing-update-owned-reads-now-0-001-other-changes-effective-april-20-2026/263025)
- [Annonce du MCP X hébergé](https://devcommunity.x.com/t/announcing-the-hosted-x-mcp/269558)
- [TechCrunch — X now offers an MCP server](https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/)
- [Guide XMCP (OpenTweet)](https://opentweet.io/blog/xmcp-x-official-mcp-server-guide)
- [X API Pricing 2026 (Postproxy)](https://postproxy.dev/blog/x-api-pricing-2026/)
