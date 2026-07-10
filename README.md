# feeds — bookmarks X → bibliothèque de savoir

Pipeline quotidien qui récupère les bookmarks X, lit leur contenu et les pages
qu'ils référencent, en extrait du savoir via Claude, et l'organise en
bibliothèque markdown versionnée. Design détaillé : [docs/reco-pinned-tweets-knowledge.md](docs/reco-pinned-tweets-knowledge.md).

## Structure

```
sources/2026/<tweet_id>-<slug>.md   # 1 note immuable par bookmark + archive des liens
notes/<topic>.md                    # notes de synthèse vivantes, mises à jour par le pipeline
taxonomy.yaml                       # vocabulaire de tags contrôlé
indexes/                            # index dérivés (par tag, par date), régénérés
state/seen_ids.json                 # déduplication
state/token.enc                     # token OAuth X, chiffré (Fernet), recommitté par la CI
pipeline/                           # le code
```

## Mise en route

1. **App développeur X** — sur [developer.x.com](https://developer.x.com) (mode
   pay-per-use) : créer une app, activer OAuth 2.0, ajouter
   `http://localhost:8484/callback` aux redirect URIs. Récupérer client ID (et
   secret si client confidentiel).

2. **Autorisation initiale** (une fois, en local) :

   ```bash
   pip install -r requirements.txt
   cp .env.example .env   # remplir X_CLIENT_ID, ANTHROPIC_API_KEY
   python scripts/authorize.py
   ```

   Le script affiche `TOKEN_ENC_KEY` (à mettre dans `.env` et à garder) et écrit
   `state/token.enc`. **Committer `state/token.enc`** — il est chiffré ; seule
   la clé est secrète.

3. **Secrets GitHub** (Settings → Secrets → Actions) : `X_CLIENT_ID`,
   `X_CLIENT_SECRET` (si confidentiel), `TOKEN_ENC_KEY`, `ANTHROPIC_API_KEY`.

4. **Premier run** :

   ```bash
   python -m pipeline.main --limit 2   # test local
   ```

   Ensuite la GitHub Action ([ingest.yml](.github/workflows/ingest.yml)) tourne
   chaque jour et committe les nouvelles notes.

## Fonctionnement

Pour chaque nouveau bookmark : le pipeline récupère le texte complet (posts
longs inclus), télécharge et archive le contenu des liens sortants (anti link
rot), demande à Claude un résumé/idées clés/tags (choisis dans
`taxonomy.yaml`), écrit la note source, puis met à jour la note de synthèse du
thème principal (fusion, déduplication, contradictions signalées).

Les tags proposés par le modèle hors vocabulaire atterrissent dans le
frontmatter `proposed_tags` des notes sources : les ajouter à `taxonomy.yaml`
à la main pour les activer.

### Note sur le token X

Les refresh tokens X sont rotatifs (usage unique). Le token vit donc dans
`state/token.enc`, chiffré avec `TOKEN_ENC_KEY`, et la CI le recommitte après
chaque refresh. Ne jamais committer la clé ni un token en clair.
