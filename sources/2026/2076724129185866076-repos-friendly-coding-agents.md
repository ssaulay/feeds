---
author: '@mikeldking'
date: '2026-07-13T17:43:10.000Z'
links: []
primary_topic: ai-agents
proposed_tags: []
tags:
- ai-agents
- dev-tools
- engineering
title: 6 pratiques pour rendre un repo compatible avec les agents de code
tweet_id: '2076724129185866076'
url: https://x.com/mikeldking/status/2076724129185866076
---

# 6 pratiques pour rendre un repo compatible avec les agents de code

> Post de **@mikeldking** — [voir sur X](https://x.com/mikeldking/status/2076724129185866076)

## Résumé

Retour d'expérience sur 6 mois de préparation de repositories pour optimiser le travail des coding agents. L'auteur détaille des pratiques concrètes : CI rapide, déclenchement automatique d'agents, tâches cron, preuves de travail (screenshots), déploiement hermétique local, et données de simulation réalistes.

## Idées clés

- Accélérer la CI avec des outils modernes (Rust/Zig/Go) comme UV, oxfmt, TypeScript 7, et déplacer les tests d'intégration en post-merge.
- Déclencher automatiquement des agents sur des labels de triage pour qu'ils préparent un POC ou des étapes de reproduction avant qu'un ingénieur ne reprenne l'issue.
- Utiliser des crons pour déléguer aux agents les tâches répétitives que les devs détestent (SDK gaps, tuning, tests de régression).
- Donner aux agents des moyens de prouver leur travail : screenshots, navigation automatisée, stockage cloud pour les assets.
- Permettre un déploiement hermétique et local de l'application (idéalement plusieurs instances simultanées) pour accélérer les itérations des agents.
- Fournir aux agents des données de simulation réalistes reflétant l'usage réel des utilisateurs pour améliorer leur pertinence.

## Citations

> Give agents ways to prove their work. Add screenshotting skills, agent-browswer, cloud storage for storing assets.

> If a coding agent can deploy the app locally, the faster it can work.

## Texte du post

Over the past 6 months we've maniacally prepped our repos to be coding agent friendly. Here are some things that worked.

1. Make CI blazing fast. Use every Rust, Zig, or Go ported tool that lets agents verify their work. This means UV, oxfmt, Typescript 7. Move integration tests to post merge hooks.

2. Trigger coding agents automatically based on triage labels. A coding agent should setup a proof of concept or repro steps automatically so an engineer can pick up the issue seamlessly.

3. Setup crons for things devs hate doing. Setup agents to fill SDK gaps, skill tuning, filling in critical regression checks.

4. Give agents ways to prove their work. Add screenshotting skills, agent-browswer, cloud storage for storing assets.

5. Make it possible to hermetically deploy your app, preferably multiple at a time. If a coding agent can deploy the app locally, the faster it can work.

6. Give the agents realistic production "simulation" data. Agents will work much better when they are working against data that looks like how your users use the product.
