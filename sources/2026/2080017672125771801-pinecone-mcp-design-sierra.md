---
author: '@btaylor'
date: '2026-07-22T19:50:32.000Z'
links:
- https://x.com/mihai/status/2080002574472929392
primary_topic: ai-agents
proposed_tags: []
tags:
- ai-agents
- dev-tools
- engineering
title: Comment Sierra a conçu le service MCP derrière Pinecone, son agent interne
tweet_id: '2080017672125771801'
url: https://x.com/btaylor/status/2080017672125771801
---

# Comment Sierra a conçu le service MCP derrière Pinecone, son agent interne

> Post de **@btaylor** — [voir sur X](https://x.com/btaylor/status/2080017672125771801)

## Résumé

Sierra a développé Pinecone, un agent interne utilisé par tous les employés pour des tâches allant du code au GTM. Mihai détaille dans un article la conception du service MCP (Model Context Protocol) qui alimente cet agent, en abordant des problématiques fines comme le contrôle d'accès et la surcharge de contexte.

## Idées clés

- Un agent interne unique (Pinecone) peut servir des cas d'usage très variés, du code au go-to-market.
- La conception d'un service MCP soulève des défis concrets d'access control pour gérer les permissions selon les utilisateurs et les données.
- La gestion de la surcharge de contexte (context overload) est un enjeu central pour maintenir la pertinence et la performance de l'agent.

## Texte du post

We recently posted about Pinecone, Sierra’s internal agent every employee uses for everything from writing code to GTM. Mihai wrote up how the Pinecone team designed the MCP service behind it, including nuanced issues like access control and context overload. Check it out: https://t.co/0cR9e0jtZw

## Archive du contenu lié

### https://x.com/mihai/status/2080002574472929392

Tweet cité @mihai : https://t.co/dRHJG908PA
