---
author: '@mr_r0b0t'
date: '2026-05-25T21:37:53.000Z'
links:
- https://microsoft.github.io/Webwright/
primary_topic: ai-agents
proposed_tags: []
tags:
- ai-agents
- dev-tools
- engineering
title: 'Webwright : Microsoft transforme les sessions de navigateur en programmes
  réutilisables pour agents'
tweet_id: '2059026191646945515'
url: https://x.com/mr_r0b0t/status/2059026191646945515
---

# Webwright : Microsoft transforme les sessions de navigateur en programmes réutilisables pour agents

> Post de **@mr_r0b0t** — [voir sur X](https://x.com/mr_r0b0t/status/2059026191646945515)

## Résumé

Webwright est un framework de Microsoft qui donne aux agents IA un terminal plutôt qu'un contrôle direct du navigateur, leur permettant de lancer, inspecter et jeter des sessions de navigation à volonté. Le résultat n'est pas seulement une tâche accomplie, mais un espace de travail durable contenant scripts, logs, captures d'écran et outils réutilisables. Le harnais reste volontairement minimal (~1K lignes) et affiche des gains significatifs sur des benchmarks de navigation longue durée.

## Idées clés

- Sépare l'agent de la session navigateur : le browser devient jetable, tandis que le code, les logs et les captures persistent dans un workspace local.
- Transforme les actions répétitives (sélection de dates, remplissage de formulaires, filtrage) en boucles et fonctions réutilisables plutôt qu'en longues chaînes d'actions primitives.
- Une tâche résolue peut être paramétrée, exportée en CLI, partagée avec d'autres agents codants et réutilisée sans être redécouverte à zéro.
- Le harnais reste minimal (Runner, Model Endpoint, Environment terminal) sans orchestration multi-agents complexe, tout en gérant compaction du contexte et validation par auto-réflexion.
- Résultats rapportés : +35,1% relatif sur un score de navigation longue durée par rapport au précédent SOTA, sur 300 tâches live à travers 136 sites.

## Citations

> Webwright: A terminal is all you need for web agents

> The output is not just a completed task, but a reusable program.

## Texte du post

Microsoft dropping a massive Playwright update geared specifically for agents, Webwright!
This is an absolute game changer for agentic browser use as every session becomes a reusable workflow
The repo includes a @NousResearch Hermes Agent skill 😍
https://t.co/mDmKCN9kV9 https://t.co/rwlKmbHPnR

## Archive du contenu lié

### https://microsoft.github.io/Webwright/

### Disposable browsers

The agent can spawn fresh browser sessions, capture screenshots only when useful, inspect failures, and rerun scripts without being trapped in a single stateful page.

Terminal-native web agents

Webwright gives the model a terminal, a local workspace, and the freedom to write code that launches, inspects, and discards browser sessions. The output is not just a completed task, but a reusable program.

Paradigm shift

Traditional web agents keep one browser session alive and predict the next click, type, or scroll. Webwright separates the agent from that session: the browser can be launched, inspected, and discarded, while code, logs, screenshots, and outputs persist in the local workspace.

The agent can spawn fresh browser sessions, capture screenshots only when useful, inspect failures, and rerun scripts without being trapped in a single stateful page.

Date selection, form filling, filtering, comparison, and extraction can become loops and functions instead of long chains of primitive browser actions.

The durable output is a workspace: exploratory scripts, action logs, screenshots, final outputs, and eventually a reusable task program.

Reported results

The report evaluates Webwright on live, long-horizon web benchmarks while preserving the simple terminal interface. The same pipeline also records critical-point screenshots, action logs, and reusable command-line tools.

Long-horizon browsing score, a 35.1% relative improvement over the previous reported SOTA.

GPT-5.4 accuracy on 300 live tasks across 136 sites with a 100-step budget.

Qwen3.5-9B on the hard split of Online-Mind2Web when augmented with crafted reusable tools.

Minimal harness

The implementation is deliberately small: a Runner, a Model Endpoint, and a terminal Environment. Each is a single module, totaling roughly 1K lines of harness code, with no multi-agent orchestration or complex planning hierarchy.

$ python final_script.py open browser search live web pages capture screenshots write action log $ python -m webwright.tools.self_reflection evaluate critical points Status: success $ ls final_runs/run_1 final_script.py final_script_log.txt screenshots/ self_reflect_result.json

Workspace trace

The trace below makes the terminal-native loop visible. The left panel shows the workspace growing as the agent creates plans, scripts, logs, screenshots, and final-run artifacts; the terminal transcript shows the generated command and command_output that produced each observation.

Capability gallery

We show webwright can craft tools for user tasks, and converted to codex skills for repeated usage, which leads to token and time saving.

Challenges handled

Giving an agent a terminal is powerful, but it creates new failure modes. Webwright keeps the harness small while adding just enough structure around completion, context, and reuse.

The agent must generate a final script, rerun it in a fresh folder, save logs and screenshots, and pass a self-reflection judgement before done is accepted.

Long coding trajectories can exceed context limits, so history is periodically compacted into summaries while the workspace keeps the concrete artifacts.

Once solved, a task script can be parameterized, exported as a CLI, shared with coding agents, and reused instead of rediscovered from scratch.

Citation

If you use Webwright in your research or build on it, please cite the repository:

```
@misc{webwright2026,
  title        = {Webwright: A terminal is all you need for web agents},
  author       = {Lu, Yadong and Xu, Lingrui and Huang, Chao and Awadallah, Ahmed},
  year         = {2026},
  howpublished = {\url{https://github.com/microsoft/Webwright}},
  note         = {GitHub repository}
}
```
