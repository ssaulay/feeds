---
author: '@vercel_dev'
date: '2026-06-12T17:54:10.000Z'
links:
- https://vercel.com/changelog/vercel-drop
primary_topic: dev-tools
proposed_tags: []
tags:
- dev-tools
- product
- engineering
title: 'Vercel Drop : déployer un site en glissant un fichier ou dossier'
tweet_id: '2065492873555100098'
url: https://x.com/vercel_dev/status/2065492873555100098
---

# Vercel Drop : déployer un site en glissant un fichier ou dossier

> Post de **@vercel_dev** — [voir sur X](https://x.com/vercel_dev/status/2065492873555100098)

## Résumé

Vercel Drop permet de déployer un projet en glissant simplement un fichier ou dossier dans le navigateur, sans Git ni CLI. L'outil détecte automatiquement le framework (Next.js, exports Bolt.new, Claude Design, Google Stitch) ou déploie les fichiers statiques tels quels. Chaque drop crée un nouveau projet avec une URL de production live en quelques secondes.

## Idées clés

- Le déploiement ne nécessite ni Git, ni CLI, ni configuration locale préalable
- Vercel détecte automatiquement le framework utilisé (ex: Next.js) et lance le build correspondant
- Les sites statiques sans framework sont déployés directement sans étape de build
- Si aucun index.html n'est présent à la racine, l'utilisateur choisit la page racine du site
- Chaque drop génère un nouveau projet ; on peut ensuite y connecter un dépôt Git pour des déploiements automatiques

## Citations

> Drop It. It's Live.

> You don't need Git, the Vercel CLI, or any local setup.

## Texte du post

Drop It. It's Live.

Drag a file or folder into your browser and Vercel Drop gives you a production URL in seconds.

https://t.co/iJvKrgiqsm https://t.co/Y302vIyxm9

## Archive du contenu lié

### https://vercel.com/changelog/vercel-drop

Vercel Drop lets you deploy a file or folder by dragging it into your browser. You don't need Git, the Vercel CLI, or any local setup.

Drop a project onto vercel.com/drop, pick a team and project name, and select **Deploy**. Vercel will create a new project, upload your files, and publish them straight to production with a live URL you can share. All in a matter of seconds.

**Vercel Drop handles more than static files:**

- Framework projects: Vercel detects your framework (e.g., Next.js) and builds it. Exports from tools like Bolt.new deploy this way.

- Static sites: Files with no framework deploy as-is, with no build step. That includes exports from Claude Design and Google Stitch. If your folder has no `index.html` at the top, you choose which page loads at your site's root.

Each drop creates a new project. To get automatic deployments on every push, connect a Git repository to the project afterwards.

Get started at vercel.com/drop or read the documentation.
