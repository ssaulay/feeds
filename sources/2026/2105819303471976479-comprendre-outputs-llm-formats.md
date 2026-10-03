---
author: '@karpathy'
date: '2026-10-02T00:37:00.000Z'
links: []
primary_topic: llm
proposed_tags: []
tags:
- llm
- prompt-engineering
- productivity
title: Stratégies de formats pour mieux comprendre les outputs des LLM
tweet_id: '2105819303471976479'
url: https://x.com/karpathy/status/2105819303471976479
---

# Stratégies de formats pour mieux comprendre les outputs des LLM

> Post de **@karpathy** — [voir sur X](https://x.com/karpathy/status/2105819303471976479)

## Résumé

Karpathy propose plusieurs techniques pour rendre les sorties des LLM plus lisibles et compréhensibles : écrire en ASD-STE100 (langage contrôlé aérospatial), générer des diagrammes, créer des pages HTML interactives, ou même des vidéos explicatives type 3b1b. L'image jointe détaille la norme ASD-STE100 (structure, règles grammaticales, formes verbales autorisées, limites de mots) comme exemple de langage contraint produisant une écriture plus claire. L'idée centrale : à mesure que les LLM autonomisent le travail, notre rôle se déplace vers la supervision et la compréhension des résultats.



## Idées clés

- Demander à un LLM d'écrire selon la norme ASD-STE100 (ou '80% de cette rigueur') produit un texte plus clair et lisible.
- Privilégier les diagrammes aux textes quand c'est possible, car ils sont plus faciles à parser visuellement.
- Demander une sortie en HTML permet d'obtenir des pages interactives et visuellement riches, exploitant les compétences frontend des LLM.
- Les vidéos explicatives générées sur mesure (style 3Blue1Brown, avec narration via API comme ElevenLabs) sont le format le plus prometteur.
- À mesure que les LLM automatisent le travail de fond, les humains doivent monter en abstraction vers la supervision et la compréhension.
- L'abondance de calcul et de code permet de créer des artefacts logiciels volumineux et jetables qui n'auraient pas eu de sens à produire manuellement avant.

## Citations

> As LLMs get better, they will do more and more of the legwork autonomously, and a lot more of our work will rise up the abstractions into oversight and understanding.

> Push the boundaries here and you'll be surprised.

## Texte du post

We'll be spending a lot more time trying to understand the outputs of language models. A few thoughts, tips & tricks:

Writing. Something I've had success with: Ask your LLM to explain something in ASD-STE100, it's a controlled language specification originally developed for aerospace maintenance documentation. LLMs well-versed in this language and it comes with heavy constraints on clean writing style that I often find a lot more readable. Sometimes I've tried to soften it a bit e.g. ask for "80% of the way to ASD-STE100" because the spec is quite stringent. But even better:

Diagrams / images. Instead of writing, ask your LLM to create a diagram. These can be a lot easier to process, parse, and understand. But even better:

Web pages. Ask for output "in HTML" to get a beautiful, interactive webpage. LLMs are getting really good at frontend and can create beautiful experiences, animations, etc. But even better:

Explainer videos. The output format I am most bullish on is fully custom / bespoke explainer videos generated on any arbitrary topic. Experiment with things like "Create a 3b1b style video explainer on X. Use my ElevenLabs API key for audio narration". (you'd need an API key for the latter or you can ask your LLM to find you decent free alternatives that use your local compute). This is actually starting to work!

In summary:
- As LLMs get better, they will do more and more of the legwork autonomously, and a lot more of our work will rise up the abstractions into oversight and understanding.
- Luckily, LLMs can help here too because as intelligence and code are increasingly abundant, you can ask for large, custom, discardable software artifacts (e.g. web apps, video explainers) that would have never made sense to create before. Push the boundaries here and you'll be surprised.
