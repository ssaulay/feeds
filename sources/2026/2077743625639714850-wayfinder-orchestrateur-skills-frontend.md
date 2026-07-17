---
author: '@mattpocockuk'
date: '2026-07-16T13:14:17.000Z'
links:
- https://x.com/WillNessAI/status/2077740031561642398
primary_topic: ai-agents
proposed_tags: []
tags:
- ai-agents
- dev-tools
- design
- prompt-engineering
title: Wayfinder comme orchestrateur de skills IA + prototypage frontend multi-variantes
tweet_id: '2077743625639714850'
url: https://x.com/mattpocockuk/status/2077743625639714850
---

# Wayfinder comme orchestrateur de skills IA + prototypage frontend multi-variantes

> Post de **@mattpocockuk** — [voir sur X](https://x.com/mattpocockuk/status/2077743625639714850)

## Résumé

Will Ness détaille comment il a créé une skill Claude dédiée au prototypage frontend, dérivée du système de grilling de Matt Pocock, qui génère 5 prototypes radicalement différents avec un picker pour comparer les variantes en direct. Il a ensuite intégré cette skill à /wayfinder, son orchestrateur de planification, pour que les tickets référencent automatiquement cette skill quand un travail frontend novateur est détecté.

## Idées clés

- Combiner /grilling et /prototype comme base pour générer 5 prototypes UI wildly différents plutôt qu'une seule proposition.
- Ajouter un picker permettant de switcher en direct entre les variantes pour faciliter le choix.
- Itérer par branches : à chaque round, sélectionner les favoris + donner du feedback pour affiner l'arbre de design.
- Utiliser /wayfinder comme orchestrateur central qui référence automatiquement des skills spécialisées (comme le prototypage frontend) dans les tickets de planification.
- Ce pattern (créer une skill spécialisée puis l'intégrer à l'orchestrateur) est réutilisable pour d'autres besoins récurrents.

## Citations

> This will not be the last time I build a cool skill and add it to Wayfinder; this is a very powerful pattern for planning work.

## Texte du post

Some extremely smart ideas in here around:

1. Using /wayfinder as an orchestrator of custom skills
2. Using a multi-phase prototyping approach which zooms in on one part of the UI at a time - but in context

Give Will a follow, this is good shit https://t.co/QbXsPrRNRL

## Archive du contenu lié

### https://x.com/WillNessAI/status/2077740031561642398

Tweet cité @WillNessAI : I built a variant of @mattpocockuk's grilling skill dedicated to frontend and it has improved how I build new apps and components.

The general idea:
1. Use /grilling and /prototype as a base
2. Tell Claude to build 5 WILDLY different prototypes
3. Tell Claude to include a picker that lets you switch between each variant live
4. Each round you select your favorite(s) + leave feedback, and Claude will walk down each branch of the design tree, helping you zoom in on your desired design

And THEN, I went and added it to /wayfinder, so whenever I make a new map and there's novel frontend work, a ticket is created specifically referencing that /grilling-frontend-prototyping needs to be invoked.

This will not be the last time I build a cool skill and add it to Wayfinder; this is a very powerful pattern for planning work.

You can find my skill here: https://t.co/4M4QPlfnp1
