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
3. **Extraction de savoir** — un appel Claude API par bookmark : résumé, idées clés,
   tags/thèmes, citations, liens vers notes existantes. Sortie structurée (JSON → markdown).
4. **Stockage** — un fichier markdown par bookmark dans `knowledge/YYYY/`,
   avec frontmatter (auteur, date, URL, tags). Un index par thème régénéré à chaque run.
   Le repo git **est** la bibliothèque : versionnée, greppable, lisible par Claude Code.
5. **Planification** — GitHub Action cron quotidienne (ou une Routine Claude Code
   si tu veux que l'extraction soit agentique plutôt qu'un simple appel API).

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
