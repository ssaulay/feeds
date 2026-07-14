---
author: '@AlfieJCarter'
date: '2026-04-10T17:19:12.000Z'
links: []
primary_topic: ai-agents
proposed_tags: []
tags:
- ai-agents
- dev-tools
- growth
- productivity
title: 'Playbook GTM pour Claude Code : structure d''un guide complet en 8 sections'
tweet_id: '2042653637306949677'
url: https://x.com/AlfieJCarter/status/2042653637306949677
---

# Playbook GTM pour Claude Code : structure d'un guide complet en 8 sections

> Post de **@AlfieJCarter** — [voir sur X](https://x.com/AlfieJCarter/status/2042653637306949677)

## Résumé

Ce post annonce un guide Notion structuré en 8 sections pour utiliser Claude Code efficacement dans un contexte GTM (Go-To-Market). Le contenu réel n'est pas accessible directement (nécessite like + commentaire), mais le post détaille la table des matières : setup initial, fichier de contexte projet, plan mode, skills GTM, MCP et optimisation de tokens, sub-agents, gestion du contexte, et déploiement de skills via Modal. Il s'agit d'un aperçu marketing plutôt que du contenu lui-même.

## Idées clés

- Un fichier 'project brain' doit être maintenu et mis à jour automatiquement par Claude quand il répète les mêmes erreurs.
- 5 skills GTM prioritaires à construire : scraping de leads, labellisation d'emails, génération de propositions, rédaction de séquences outbound, onboarding client.
- Convertir des MCP en skills peut réduire la consommation de tokens de 50 à 100x.
- Les sub-agents n'ont de valeur que dans 3 cas précis, avec une logique de fiabilité pour les runs parallèles.
- Le contexte se remplit avant même de taper une requête ; /compact et /clear doivent être utilisés à bon escient selon le modèle (parent vs sub-agent).
- N'importe quelle skill peut être déployée en URL live via Modal en moins de 2 minutes, connectable à n8n, Make ou Zapier.

## Texte du post

I put the entire Claude Code GTM Engineering Playbook into ONE Notion doc.

8 sections. No fluff.

- How to get set up correctly from day one: Pro plan, terminal install across Mac, Linux, and Windows, GUI install via Antigravity or VS Code, and bypass permissions mode
- What to put in your project brain file, what to leave out, and how to get Claude to update it automatically when it keeps making the same mistake
- How to run plan mode step by step and when to skip it for simple tasks
- How to build a skill file from scratch, fix one that keeps failing, and install 5 GTM skills worth building first: lead scraping, email labeling, proposal generation, outbound sequence writing, and client onboarding
- MCP install process, token cost checks after every install, the best MCPs for GTM work, and how to cut token usage by 50 to 100x by converting MCPs into skills
- Sub-agents and agent teams: the 3 cases where they earn their cost, reliability math for parallel runs, and how to enable parallel variant exploration
- What is eating your context before you type anything, how to use /compact and /clear correctly, and model selection for parent vs sub-agents
- Modal deployment: any skill as a live URL in under 2 minutes, form interface setup, and connection to n8n, Make, or Zapier

This is the setup I would have KILLED for before spending months piecing together how to actually get productive in Claude Code from documentation, YouTube tutorials, and scattered GitHub threads.

Like + comment "CODE" and I'll send it over

(must be connected for priority access)
