---
author: '@trq212'
date: '2026-05-18T16:54:29.000Z'
links:
- https://x.com/trq212/status/2056415974568710421
primary_topic: prompt-engineering
proposed_tags: []
tags:
- prompt-engineering
- ai-agents
- dev-tools
title: Maintenir un fichier implementation-notes.html pour combler les ambiguïtés
  de spec avec un agent IA
tweet_id: '2056418157305454805'
url: https://x.com/trq212/status/2056418157305454805
---

# Maintenir un fichier implementation-notes.html pour combler les ambiguïtés de spec avec un agent IA

> Post de **@trq212** — [voir sur X](https://x.com/trq212/status/2056418157305454805)

## Résumé

L'auteur propose un prompt à utiliser lors de l'implémentation d'une spec par un agent IA : maintenir en continu un fichier implementation-notes.html documentant décisions de design, déviations, compromis et questions ouvertes. L'idée répond au fait qu'aucune spec n'est jamais totalement exhaustive, il reste toujours des zones grises et des inconnues à traiter. Ce fichier donne à l'agent une marge de décision légitime tout en gardant l'humain informé et dans la boucle.

## Idées clés

- Même une spec détaillée laisse des ambiguïtés et inconnues que l'agent doit résoudre en cours de route.
- Demander à l'agent de documenter en temps réel ses choix de design, déviations, compromis et questions ouvertes dans un fichier dédié.
- Ce fichier sert de trace d'audit et de point de synchronisation entre l'humain et l'agent sans bloquer le flux de travail.
- Donner explicitement à l'agent la permission de prendre des décisions crée un meilleur résultat qu'exiger une conformité stricte impossible à la spec.

## Citations

> as much as you spec there are always still ambiguities and unknown unknowns that come up and this gives the model a good out to make decisions but keep you in the loop

## Texte du post

okay this is going kinda viral and tbh my original text was kind of messy, so here's a second pass with the help of Claude:

--
Implement <SPEC>. As you work maintain a running implementation-notes.html file that captures anything I should know about how the implementation diverges from or interprets the spec, including:

- Design decisions: choices you made where the spec was ambiguous
- Deviations: places where you intentionally departed from the spec, and why
- Tradeoffs:  alternatives you considered and why you picked what you did
- Open questions: anything you'd want me to confirm or revise

## Archive du contenu lié

### https://x.com/trq212/status/2056415974568710421

En réponse à @trq212 : as much as you spec there are always still ambiguities and unknown unknowns that come up and this gives the model a good out to make decisions but keep you in the loop
