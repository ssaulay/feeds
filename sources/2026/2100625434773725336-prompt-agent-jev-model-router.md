---
author: '@rileybrown'
date: '2026-09-17T16:38:26.000Z'
links:
- https://x.com/agentnative_/status/2100624941326500122
primary_topic: ai-agents
proposed_tags: []
tags:
- ai-agents
- dev-tools
- prompt-engineering
- llm
title: Prompt unique pour builder un agent avec routage de modèle automatique via
  Jev
tweet_id: '2100625434773725336'
url: https://x.com/rileybrown/status/2100625434773725336
---

# Prompt unique pour builder un agent avec routage de modèle automatique via Jev

> Post de **@rileybrown** — [voir sur X](https://x.com/rileybrown/status/2100625434773725336)

## Résumé

Un prompt prêt à l'emploi permet de demander à Claude ou Codex de construire une application agentique complète utilisant eve de Vercel et Jev (by Typesafe) comme routeur de modèle. L'agent peut chercher sur le web, créer des fichiers, et sélectionne automatiquement le modèle le plus adapté (cheap/medium/frontier) selon la complexité de la requête pour économiser des tokens. L'interface met en avant visuellement le choix de modèle fait par Jev en temps réel.

## Idées clés

- Un seul prompt suffit pour faire construire par un LLM (Claude/Codex) un agent complet avec routage de modèle intégré.
- Jev sert de routeur intelligent qui choisit entre modèles cheap, medium et frontier selon la complexité de la tâche pour optimiser les coûts.
- Vercel AI Gateway donne un accès unifié à tous les modèles via une seule clé API.
- Le prompt insiste pour que l'UI expose clairement et en inline le raisonnement/choix de modèle fait par Jev, comme feature centrale de l'app.
- La méthode inclut un cycle d'itération : lire la doc de Jev, tester et affiner jusqu'à ce que le routage soit vraiment efficace.

## Citations

> I want you to use jev by typesafe as a model router, make a model router for this. i want you to use it to select the best model for the job to save tokens and clearly show, as it's happening when jev chooses which model to use.

> make the wrapper beautiful and the main focus should be the inline jev selection, and how that selection was made.

## Texte du post

In one prompt you can build an agent, with every model, with a built in model router powered by Jev. 

All you need is a vercel api key. 
(Vercel Gateway has Jev).

Just ask codex or claude to build it full prompt in the post below ⬇️ https://t.co/rhpck1A0bj

## Archive du contenu lié

### https://x.com/agentnative_/status/2100624941326500122

Tweet cité @agentnative_ : Jev can be used as a model router. 

You can try this yourself using Claude or Codex... and build an agent with this single prompt using @eve by Vercel. With AI gateway you will get immediate access to every model.

Use this prompt: 

---
I want you to build a new app that uses eve. I want to make an agent that can search the web, create files and anything else an agent might be able to do. use eve you should have vercel key. 

I want you to use jev by typesafe as a model router, make a model router for this. i want you to use it to select the best model for the job to save tokens and clearly show, as it's happening when jev chooses which model to use. read the docs for jev, and make it very effective, and test it and make refinements until it's fully ready. For simple queries it should use cheap models. For more complex queries it should use frontier models and have a scale in between for medium questions.

make this then run it locally so i can test it. Make the wrapper beautiful and the main focus should be the inline jev selection, and how that selection was made.
---
https://t.co/KdDJopEcHo
