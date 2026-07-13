---
author: '@lennysan'
date: '2026-04-24T13:29:29.000Z'
links:
- https://www.youtube.com/watch?v=PplmzlgE0kg
primary_topic: product
proposed_tags: []
tags:
- product
- ai-agents
- management
- dev-tools
title: 'Comment l''équipe Claude Code d''Anthropic ship vite : leçons de Cat Wu'
tweet_id: '2047669259380383955'
url: https://x.com/lennysan/status/2047669259380383955
---

# Comment l'équipe Claude Code d'Anthropic ship vite : leçons de Cat Wu

> Post de **@lennysan** — [voir sur X](https://x.com/lennysan/status/2047669259380383955)

## Résumé

La Head of Product de Claude Code partage comment Anthropic est passé de cycles produit de six mois à des cycles d'un jour, en fusionnant les rôles PM/ingénieur/designer autour du "goût produit". L'équipe construit délibérément des produits à la limite du fonctionnel pour pouvoir tester immédiatement chaque nouveau modèle, et audite régulièrement ses prompts système pour retirer les béquilles devenues inutiles.

## Idées clés

- Les cycles produit sont passés de 6 mois à parfois 1 jour grâce aux research previews et à un 'launch room' permanent.
- Le rôle de PM évolue vers l'habilitation d'expéditions quotidiennes plutôt que la coordination de roadmaps trimestrielles.
- L'unité de production la plus efficace est un ingénieur avec du goût produit, sans PM intermédiaire.
- Construire des produits à la limite du fonctionnement permet de tester immédiatement chaque nouveau modèle et d'éviter d'être un cycle en retard.
- Demander au modèle d'introspecter sur ses erreurs révèle les failles du prompt système ou du harnais.
- Chaque nouveau modèle doit déclencher un audit du prompt système pour retirer les béquilles devenues inutiles (dette technique).
- Les employés Anthropic construisent leurs propres outils internes (Claude Code, Cowork, Slack) plutôt que d'acheter du SaaS.
- La personnalité de Claude (low-ego, positive, earnest) est un facteur clé de succès, pas un détail cosmétique.
- Le futur du travail est la gestion de flottes d'agents IA (50-100 tâches simultanées), pas l'exécution directe.
- Recruter des personnes qui accueillent le chaos avec optimisme est essentiel face à l'accélération du rythme de l'IA.

## Citations

> There should be less emphasis on making sure you are aligning your multi-quarter roadmaps with your partner teams and more emphasis on, OK, how can we figure out the fastest way to get something out the door?

> When you reflect on everyone you've worked with, there's just some people where you're like, I really like their energy, their vibe.

## Texte du post

My biggest takeaways from Claude Code's Head of Product @_catwu:

1. Anthropic’s product development timelines have gone from six months to one month, sometimes one week, sometimes one day. Part of this acceleration is access to the latest models (i.e. Mythos). Another is shipping new products into “research preview,” making clear it's early, experimental, and might not be supported forever. Another is an evergreen "launch room "where engineers post ready features and marketing turns around announcements the next day.

2. The PM role is shifting from coordinating multi-month roadmaps to enabling teams to ship daily. As Cat puts it, “There should be less emphasis on making sure you are aligning your multi-quarter roadmaps with your partner teams and more emphasis on, OK, how can we figure out the fastest way to get something out the door?”

3. The most efficient shipping unit is an engineer with great product taste. On Cat’s team, many engineers go end-to-end—from seeing user feedback on Twitter to shipping a product by the end of the week—without a PM involved. Also, almost all the PMs on the Claude Code team have either been engineers or ship code themselves, and the designers have been front-end engineers. The roles are merging, and the most valuable skill is product taste, not job title.

4. Build products that are on the edge of working. Claude Code’s code review product failed multiple times because earlier models weren’t accurate enough. But because the prototype was already built, they could swap in Opus 4.5 and 4.6 and immediately test whether the gap was closed. Teams that wait for the model to be ready will always be a cycle behind.

5. The most underrated skill for building AI products is asking the model to introspect on its own mistakes. Cat regularly asks the model why it made an unexpected decision. The model will explain that something in the system prompt was confusing, or that it delegated verification to a subagent that didn’t check its work. This reveals what misled the model so the team can fix the harness.

6. Every model release forces their team to revisit existing products and audit their system prompt to remove features the model no longer needs. Claude Code’s to-do list was a crutch for earlier models that couldn’t track their own work. With Opus 4, the model handles it natively. Features built as scaffolding for weaker models become debt when the model catches up—so the team actively strips them.

7. Anthropic employees build custom internal tools instead of buying SaaS products. A sales team member built a web app that pulls from Salesforce, Gong, and call notes to auto-customize pitch decks—work that used to take 20 to 30 minutes now takes seconds. Their core stack is Claude Code, Cowork, and Slack. No Notion, no Linear, no Figma.

8. People underestimate how much Claude’s personality contributes to its success. As Cat describes it, “When you reflect on everyone you’ve worked with, there’s just some people where you’re like, I really like their energy, their vibe.” Claude is designed to be low-ego, positive, competent, and earnest—qualities that make it feel like a great coworker, not just a tool. This isn’t cosmetic; it’s what makes people want to use Claude for hours every day. The team has a dedicated person, Amanda, who “molds Claude’s character,” and it’s one of the hardest roles at the company because success is so subjective.

9. The future of work is managing fleets of AI agents, not doing the work yourself. Cat sees a clear progression: first, individual tasks become successful. Then people start running multiple tasks at the same time (multi-Clauding). Next, people will run 50 or 100 tasks simultaneously, which will require new infrastructure—remote execution, better interfaces for managing tasks, agents that fully verify their work, and self-improving systems that incorporate feedback. The human role shifts from doing the work to knowing which tasks to look into, verifying outputs, and giving feedback that makes the system better over time.

10. Hire people who lean into chaos and face every challenge with a smile. At Anthropic, there are weeks when a P0 on Sunday becomes a P00 by Monday and a P000 by Monday afternoon. If you get too stressed about any one thing, you’ll burn out. Their team looks for people who can look at a hard challenge and say, “Wow, that’s gonna be hard. But I’m excited to tackle it and I’m gonna do the best that I possibly can.” This mindset—optimism, resilience, and comfort with constant change—is increasingly essential as the pace of AI development accelerates.

Don't miss the full conversation: https://t.co/1wOUHcdYQN

## Archive du contenu lié

### https://www.youtube.com/watch?v=PplmzlgE0kg

About
Press
Copyright
Contact us
Creators
Advertise
Developers
Terms
Privacy
Policy & Safety
How YouTube works
Test new features
NFL Sunday Ticket
© 2026 Google LLC
