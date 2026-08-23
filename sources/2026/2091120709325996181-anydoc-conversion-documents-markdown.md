---
author: '@sidequestforevr'
date: '2026-08-22T11:10:02.000Z'
links:
- https://x.com/SylvainDeaure/status/2090776807578468538
primary_topic: dev-tools
proposed_tags: []
tags:
- dev-tools
- ai-agents
- engineering
title: 'Anydoc de Firecrawl : conversion universelle de documents vers Markdown, ultra-rapide
  et locale'
tweet_id: '2091120709325996181'
url: https://x.com/sidequestforevr/status/2091120709325996181
---

# Anydoc de Firecrawl : conversion universelle de documents vers Markdown, ultra-rapide et locale

> Post de **@sidequestforevr** — [voir sur X](https://x.com/sidequestforevr/status/2091120709325996181)

## Résumé

Firecrawl a open-sourcé anydoc, un convertisseur de documents (docx, pptx, xlsx, PDF, epub, rtf...) vers Markdown, écrit en Rust pur, 100% local et sans modèle ML. Il affiche des performances remarquables (médiane ~5ms vs 1100ms pour LibreOffice) et une détection de format basée sur le contenu plutôt que l'extension, utile pour repérer les fichiers corrompus. Idéal pour intégrer une conversion synchrone de documents dans une boucle d'agent IA sans gestion asynchrone complexe.

  

## Idées clés

- Anydoc convertit 14 formats de documents vers un Markdown unifié (GFM) avec des règles cohérentes quel que soit le format source.
- Performances très élevées : 500 docx convertis en 1,7s, permettant une intégration synchrone dans une boucle d'agent sans file d'attente async.
- La détection de format se fait par analyse du contenu et non de l'extension, ce qui rejette proprement les faux fichiers et peut servir à détecter des fichiers corrompus dans un dossier.
- L'outil est honnête sur ses limites : un PDF scanné renvoie 'Unsupported' plutôt qu'un résultat approximatif, laissant l'OCR à la charge de l'utilisateur.
- Intégration simple pour les agents IA via une seule commande : npx skills add firecrawl/anydoc.
- Gestion des erreurs par catégorie (encrypted, unsupported, malformed) même en version 0.1.x, avec un taux de succès de 98% sur des fichiers valides.

## Citations

> Détection par CONTENU, pas par extension : un faux .docx (du JSON renommé) est refusé proprement.

> Il est honnête : un PDF scanné renvoie « Unsupported » au lieu d'une bouillie best effort.

## Texte du post

Un poste bien sympa pour tous ceux qui font de l'agentique.

Au passage le compte de Sylvain et sûrement un des plus sous côté du X francophone https://t.co/eza2YgnEf2

## Archive du contenu lié

### https://x.com/SylvainDeaure/status/2090776807578468538

Tweet cité @SylvainDeaure : Si tes agents (Claude, Hermès...) mangent du document, regarde ça : Firecrawl vient d'open-sourcer anydoc 🔥

Un convertisseur universel → Markdown, 100 % local, en Rust pur. 14 formats (docx, pptx, xlsx, PDF, epub, rtf...), médiane ~5 ms là où LibreOffice met 1 100 ms. Zéro cloud, zéro modèle ML.

Ce qui m'a plu en creusant 🧭

⚡ 500 docx → Markdown en 1,7 s. De quoi brancher la conversion en synchrone dans une boucle d'agent, sans file d'attente asynchrone ni callbacks.

🕵️ Détection par CONTENU, pas par extension : un faux .docx (du JSON renommé) est refusé proprement. Bonus inattendu : passe-le sur un vieux dossier, les fichiers signalés « malformed » sont ta liste de fichiers corrompus. Personne ne l'a conçu pour ça, ça marche quand même.

📐 Sortie unifiée en GitHub-Flavored Markdown : niveaux de titres, cellules fusionnées, notes de bas de page, speaker notes des slides : les mêmes règles quel que soit le format d'entrée, un .doc de 2003 ou un .pptx d'hier.

🤝 Et il est honnête : un PDF scanné renvoie « Unsupported » au lieu d'une bouillie best effort. L'OCR reste ton affaire.

Les médianes réelles par format (tests communauté, 206 fichiers) : csv/xlsx sous 5 ms, docx ~6 ms, pptx et pdf ~22 ms. Compte ~20 s pour 1 000 pptx. Succès : 98 % une fois écartés les faux fichiers. Encore en 0.1.x : en prod, gère les erreurs par catégorie (encrypted, unsupported, malformed).

Intégration agent en une ligne :
npx skills add firecrawl/anydoc
et ton agent convertit seul les documents qu'il croise.

https://t.co/SFaclkPDUZ
