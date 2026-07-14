---
author: '@brivael'
date: '2026-04-22T17:23:14.000Z'
links:
- https://x.com/googleaidevs/status/2046990222408200316
primary_topic: llm
proposed_tags: []
tags:
- llm
- data
- dev-tools
title: 'Gemini Embedding 2 : un seul espace vectoriel pour texte, image, audio, vidéo
  et PDF'
tweet_id: '2047003304937332860'
url: https://x.com/brivael/status/2047003304937332860
---

# Gemini Embedding 2 : un seul espace vectoriel pour texte, image, audio, vidéo et PDF

> Post de **@brivael** — [voir sur X](https://x.com/brivael/status/2047003304937332860)

## Résumé

Google lance Gemini Embedding 2, un modèle d'embedding nativement multimodal qui unifie texte, image, vidéo (jusqu'à 2 min), audio natif et PDF dans un seul espace vectoriel de 3072 dimensions. Il remplace les pipelines à plusieurs modèles (CLIP, Whisper, etc.) qu'il fallait aligner manuellement, avec des gains de performance (68.32 sur MTEB) et de latence (-70% chez Sparkonomy). Entraîné en Matryoshka Representation Learning, il permet de tronquer les vecteurs à 768 dimensions sans perte de qualité, réduisant coûts de stockage et de recherche.

## Idées clés

- Un seul modèle et un seul espace vectoriel remplacent les stacks multi-modèles (CLIP + Whisper + embedder texte) auparavant nécessaires pour du RAG multimodal.
- L'audio est encodé nativement sans passer par une transcription, ce qui permet d'indexer des podcasts directement dans le même espace que du texte.
- La recherche cross-modale (texte + image simultanément) devient possible sans avoir à stitcher deux vector stores séparés.
- Le Matryoshka Representation Learning permet de tronquer le vecteur de 3072 à 768 dimensions sans perte de qualité, divisant le stockage par 4.
- Prix très compétitif (0.20$/M tokens, 0.10$ en batch) rendant l'indexation à grande échelle abordable.
- Stratégiquement, Google construit des briques d'infrastructure qui rendent obsolètes plusieurs produits concurrents à la fois, pendant que la concurrence communique surtout via des démos.

## Citations

> Le control layer se fait grignoter par le bas pendant qu'OpenAI fait des démos. Again.

## Texte du post

Google vient de sortir Gemini Embedding 2 et c'est un game changer pour le RAG.

Pour comprendre pourquoi, faut d'abord expliquer ce qu'est un embedding.

Un embedding c'est une façon de transformer n'importe quel contenu (texte, image, son, vidéo) en une liste de nombres. Un vecteur. Et la magie c'est que deux contenus qui veulent dire la même chose se retrouvent proches dans cet espace mathématique. "Chat" et "félin" finissent collés. "Chat" et "grille-pain" sont à l'opposé.

C'est ce qui permet à un moteur de recherche de comprendre ton intention au lieu de juste matcher des mots clés. C'est la brique de base de tout système RAG moderne, de toute recherche sémantique, de toute base vectorielle.

Jusqu'ici le problème c'était que chaque modalité avait son propre modèle. CLIP pour les images, Whisper + un embedder texte pour l'audio, un autre truc pour la vidéo. Des vecteurs incompatibles, des pipelines à 3 ou 4 modèles qu'il fallait stitcher à la main, et un cauchemar d'alignement.

Gemini Embedding 2 écrase tout ça. Un seul modèle, un seul espace vectoriel de 3072 dimensions, cinq modalités dedans : texte, image, vidéo jusqu'à 2 min, audio natif (sans passer par une transcription), et PDF.

Concrètement ça veut dire que tu peux :

Envoyer une requête texte "le moment où le client pleure" et retrouver la séquence exacte dans 4000 heures de réunions Zoom.

Chercher "chaussures de running bleues minimalistes" dans un catalogue e-commerce et que le modèle matche sur le texte ET l'image produit en même temps, sans avoir à aligner deux vector stores.

Indexer des podcasts sans les transcrire. L'audio va direct dans le même espace que tes docs texte.

Les chiffres sont brutaux. 68.32 sur MTEB English, 5 points d'avance sur le suivant. 68.8 sur la retrieval vidéo contre 60 pour Amazon Nova 2. Sparkonomy rapporte 70% de latence en moins après avoir remplacé leur pipeline à 3 modèles par celui-ci.

Cerise sur le gâteau, c'est entrainé en Matryoshka Representation Learning. Tu peux tronquer le vecteur de 3072 à 768 dimensions sans perdre en qualité. Stockage divisé par 4, recherche plus rapide, factures réduites.

Prix : 0.20$ par million de tokens, 0.10$ en batch. Pour 1 million de docs de 500 tokens, ça te coûte 50 balles.

La leçon stratégique : Google continue de faire ce qu'il fait de mieux. Pas de hype, pas de tweet sassy, juste une brique d'infrastructure qui rend obsolète trois produits concurrents d'un coup. Et qui s'intègre directement dans leur stack Vertex AI.

Le control layer se fait grignoter par le bas pendant qu'OpenAI fait des démos. Again.

## Archive du contenu lié

### https://x.com/googleaidevs/status/2046990222408200316

Tweet cité @googleaidevs : Gemini Embedding 2 is now generally available in the Gemini API and Vertex AI!

Start building with our first natively multimodal embedding model, now equipped with the stability and optimizations required for production apps. https://t.co/howDTPbG1Q
