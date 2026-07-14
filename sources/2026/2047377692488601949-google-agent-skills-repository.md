---
author: '@GoogleCloudTech'
date: '2026-04-23T18:10:54.000Z'
links:
- https://goo.gle/4eCsZqu
primary_topic: ai-agents
proposed_tags: []
tags:
- ai-agents
- dev-tools
- engineering
title: Google lance son dépôt officiel Agent Skills pour enrichir les agents IA
tweet_id: '2047377692488601949'
url: https://x.com/GoogleCloudTech/status/2047377692488601949
---

# Google lance son dépôt officiel Agent Skills pour enrichir les agents IA

> Post de **@GoogleCloudTech** — [voir sur X](https://x.com/GoogleCloudTech/status/2047377692488601949)

## Résumé

Google Cloud annonce le lancement de son dépôt officiel Agent Skills sur GitHub, un format ouvert pour doter les agents IA de nouvelles capacités et expertises via une documentation compacte au format Markdown. Ce dépôt démarre avec treize skills couvrant des produits Google Cloud (BigQuery, Firebase, GKE, etc.), des piliers d'architecture bien conçue, et des recipes pour l'onboarding, l'authentification et l'observabilité réseau. L'objectif est d'éviter le 'context bloat' causé par une utilisation excessive des serveurs MCP.

## Idées clés

- Les Skills sont une documentation compacte et agent-first écrite en Markdown, chargée uniquement à la demande pour réduire le risque de surcharge de contexte.
- Contrairement aux serveurs MCP qui peuvent charger d'énormes quantités de contexte et confondre le modèle, les Skills offrent une expertise condensée et ciblée.
- Le dépôt est installable facilement via 'npx skills install github.com/google/skills' et compatible avec Antigravity, Gemini CLI et des agents tiers.
- Le dépôt démarre avec 13 skills et sera enrichi progressivement dans les semaines et mois à venir.

## Citations

> Skills are a simple, open format for giving agents new capabilities and expertise. Think of a skill as compact, agent-first documentation for a specific technology or task.

## Texte du post

Our official Agent Skills repository on @github is here!

Skills are a simple, open format for giving agents new capabilities and expertise. Think of a skill as compact, agent-first documentation for a specific tech or task.

Learn more → https://t.co/7w887vz3lE #GoogleCloudNext https://t.co/ltPAgCSUaU

## Archive du contenu lié

### https://goo.gle/4eCsZqu

# Level Up Your Agents: Announcing Google's Official Skills Repository

##### Megan O'Keefe

Senior Staff Developer Advocate

As AI models improve, technical practitioners are increasingly turning to agentic AI tools to build with Google Cloud products, from Firebase and the Gemini API, to BigQuery and GKE.  But how can you ensure that the model is equipped with **accurate, up-to-date information **about these technologies? 

One way to do this is to plug your AI agent into a grounded, real-time information source. For instance, Google offers a Model Context Protocol (MCP) server for its developer documentation. But heavily using MCP servers can cause a problem called “context bloat,” where huge amounts of context are loaded into the context window, confusing the model and racking up token costs.

We need a way to equip agents with additional, condensed expertise — and we can do this with **Agent Skills.**** **

Skills are “a simple, open format for giving agents new capabilities and expertise.” Think of a skill as compact, agent-first documentation for a specific technology or task. Skills are written in Markdown and can contain reference files, code snippets, and other assets. Agents load in skill information only as-needed, reducing the risk of context bloat.

Today, on Day 1 of Google Cloud Next 2026, we’re excited to announce the launch of Google’s official Agent Skills repository:

This repository is starting off with thirteen skills, focused on Google Cloud technologies:

- 
A selection of products **:**AlloyDB, BigQuery, Cloud Run, Cloud SQL, Firebase, Gemini API, and Google Kubernetes Engine (GKE).
- 
Three **Well-Architected Pillar**- 
“Recipe” skills for Google Cloud Onboarding, Authentication, and Network Observability. 

Use `npx skills install ``github.com/google/skills` to install these skills to your agents of choice, including Antigravity, Gemini CLI, and third-party agents. 

Stay tuned as we launch additional skills in this repo in the coming weeks and months!

Now get building!
