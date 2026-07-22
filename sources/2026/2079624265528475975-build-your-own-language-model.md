---
author: '@felixrieseberg'
date: '2026-07-21T17:47:17.000Z'
links:
- http://languagemodelbuilder.com
primary_topic: llm
proposed_tags: []
tags:
- llm
- engineering
- dev-tools
title: Un manuel interactif pour construire son propre modèle de langage
tweet_id: '2079624265528475975'
url: https://x.com/felixrieseberg/status/2079624265528475975
---

# Un manuel interactif pour construire son propre modèle de langage

> Post de **@felixrieseberg** — [voir sur X](https://x.com/felixrieseberg/status/2079624265528475975)

## Résumé

Felix Rieseberg présente une application/textbook interactive qui enseigne les fondamentaux du pré-entraînement d'un modèle de langage, accessible sans expérience en programmation ou en machine learning. L'outil permet de manipuler concrètement tokenizer, embeddings, attention et courbes d'entraînement pour comprendre comment un modèle apprend. L'exemple montré utilise une recette d'entraînement type nanoGPT sur le dataset TinyStories.

Cette approche pédagogique combine théorie accessible et pratique immédiate via des playgrounds intégrés (visualisation de la loss curve, réglages du learning rate, warmup, batch size), rendant tangible un domaine souvent perçu comme abstrait ou réservé aux experts.

## Idées clés

- Un textbook interactif permet d'expérimenter directement les concepts (tokenizer, embeddings, attention, entraînement) sans coder
- Le contenu est conçu pour être accessible aux non-programmeurs tout en offrant des approfondissements optionnels pour les curieux
- L'exemple pratique utilise une petite recette de type nanoGPT (25M params) entraînée sur TinyStories, avec warmup linéaire puis décroissance cosinus du learning rate
- AdamW est appliqué uniquement aux poids de multiplication matricielle, en laissant RMSNorm et les embeddings hors régularisation
- Le projet vise à démystifier le pré-entraînement en montrant concrètement l'évolution de la loss curve et du texte généré au fil des checkpoints

## Citations

> It's so much fun to chat with something you made.

> The educational content is only as long as it needs to be, without generated filler content.

## Texte du post

Have you built a language model? You should. It's so much fun to chat with something you made.

Anyone can do it, too. I made an app that teaches the fundamentals and gives you everything you need to build your own: https://t.co/nLjFfpczbV https://t.co/akIMnTzOEG

## Archive du contenu lié

### http://languagemodelbuilder.com

### A short textbook with interactive playgrounds

I often find myself explaining how language models are built and trained to friends and family. I finally wrote the introduction I always wanted: It’s friendly to non-programmers, contains many interactive examples, and covers all the fundamentals without treating the reader like a child or a machine learning expert.

- #### Interactive from the first page- Run the experiments yourself: build a tokenizer, move through embedding space, inspect attention, and watch a tiny model learn. 
- #### Go as deep as you like- No coding, machine learning, or math experience required. Where useful, I’ve added opportunities for those curious to dive a little deeper. 
- #### No artificial additives- The educational content is only as long as it needs to be, without generated filler content.
