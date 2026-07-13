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
title: 'Vercel Drop : déployer un site en glissant un dossier dans le navigateur'
tweet_id: '2065492873555100098'
url: https://x.com/vercel_dev/status/2065492873555100098
---

# Vercel Drop : déployer un site en glissant un dossier dans le navigateur

> Post de **@vercel_dev** — [voir sur X](https://x.com/vercel_dev/status/2065492873555100098)

## Résumé

Vercel Drop permet de déployer un fichier ou dossier en le glissant directement dans le navigateur, sans Git ni CLI. L'outil détecte automatiquement les frameworks (Next.js) ou déploie des sites statiques tels quels, générant une URL de production en quelques secondes.

## Idées clés

- Le déploiement se fait sans installation locale : glisser-déposer un fichier ou dossier sur vercel.com/drop suffit.
- Vercel détecte automatiquement le framework utilisé (ex: Next.js) et lance le build correspondant.
- Les sites statiques (exports de Claude Design, Google Stitch, Bolt.new) sont déployés directement sans étape de build.
- Chaque drop crée un nouveau projet ; connecter un repo Git ensuite permet d'automatiser les futurs déploiements.

## Citations

> Vercel Drop lets you deploy a file or folder by dragging it into your browser. You don't need Git, the Vercel CLI, or any local setup.

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
