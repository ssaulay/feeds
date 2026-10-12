---
author: '@hanakoxbt'
date: '2026-10-10T21:36:18.000Z'
links:
- https://x.com/hanakoxbt/status/2091515787366306154
primary_topic: prompt-engineering
proposed_tags: []
tags:
- prompt-engineering
- ai-agents
- dev-tools
- engineering
title: Un prompt-harness pour transformer Opus 5.5 en agent qui termine vraiment ses
  tâches
tweet_id: '2109035317684834669'
url: https://x.com/hanakoxbt/status/2109035317684834669
---

# Un prompt-harness pour transformer Opus 5.5 en agent qui termine vraiment ses tâches

> Post de **@hanakoxbt** — [voir sur X](https://x.com/hanakoxbt/status/2109035317684834669)

## Résumé

Boris Cherny (créateur de Claude Code) a publié un prompt structuré qui transforme Opus 5.5 en un véritable harness d'exécution plutôt qu'une simple conversation. Le prompt organise le travail en 7 couches (plan, contexte, outils/hooks, permissions, vérification, feedback, completion) avec des fichiers de suivi (plan.md, checks.md, progress.md, CLAUDE.md) pour garantir fiabilité et traçabilité.

## Idées clés

- Traiter chaque tâche comme un harness structuré (plan + contexte + outils + checks + règles) plutôt qu'un long chat unique.
- Toujours entrer en mode plan et faire valider le plan avant d'éditer quoi que ce soit.
- Transformer les règles déterministes en hooks/scripts plutôt qu'en simples instructions dans le prompt, car un prompt reste du jugement et non une garantie.
- Chaque étape doit être vérifiée avec des signaux réels (tests, builds, type checks, screenshots) et consignée dans checks.md.
- Construire une boucle de feedback en deux temps : correction (renvoyer l'étape avec raison/preuve, limité à 3 tentatives) et mémoire (écrire la règle dans CLAUDE.md pour que l'erreur ne se reproduise plus).
- Avant de livrer, produire une checklist de complétion vérifiable (sortie existante, checks passés, erreurs corrigées ou signalées).
- Documenter l'avancement via progress.md à chaque étape pour permettre une reprise propre en cas d'interruption.
- Limiter le scope des éditions et exiger une validation avant publication, envoi ou dépense d'argent.

## Citations

> Complete {{TASK}} inside a harness, not one long chat.

> Do not weaken a check to obtain a pass.

> When it makes a mistake, add the rule to CLAUDE.md.

## Texte du post

Boris Cherny (Claude Code creator) just released a prompt that turns Opus 5.5 into a harness that actually finishes any job.

It's f*cking unreal...

Send it to Opus 5.5, and thank me later. Then read the full guide for Opus 5.5 Graph Engineering. https://t.co/DEPUCvY3lM https://t.co/fEPJmINT63

## Archive du contenu lié

### https://x.com/hanakoxbt/status/2091515787366306154

Tweet cité @hanakoxbt : https://t.co/5w8ILIIelz
