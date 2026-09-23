# design

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Trois apports dessinent un paysage du design assisté par IA organisé autour d'un même axe : gouvernance/règles explicites vs. fluidité/génération libre.

**DESIGN.md** (Google) est un format markdown encodant les règles de design (couleurs, typographie, spacing, composants) de façon portable entre outils (Stitch, agents de code, builders). Objectif : une mémoire de projet réutilisable garantissant la cohérence visuelle de l'exploration initiale à l'implémentation, en servant de garde-fou aux agents IA.

Les **10 UI Skills** (catalogue *UI Skills*) prolongent cette logique de contrainte explicite mais à un grain plus fin : au lieu d'un fichier de règles projet unique, ce sont des fichiers d'instructions spécialisés par expertise, activables à la demande pour un agent de design engineering :
- *frontend-design* : éviter les clichés visuels générés par IA (crème+serif+terracotta, cartes SaaS uniformes, eyebrows en majuscules), ancrer les choix dans le produit réel.
- *apple-design* : traduire les principes WWDC (réponse instantanée, manipulation directe, interruptibilité, springs plutôt que durées fixes) en interfaces web fluides.
- *beautiful-shadows* : classes Tailwind précises pour une élévation neutre, contre les ombres génériques.
- *accessibility* : audit structuré autour de WCAG 2.2 (POUR), outillé (Lighthouse, arbre d'accessibilité), incluant les nouveautés 2.2 (cible tactile 24×24px).
- *design-review* : critique senior classée par sévérité (Blocking/Important/Polish), avec preuve fichier:ligne plutôt que checklist générique.
- *emil-design-eng* : cadre de décision pour l'animation (faut-il animer ? easing ? durée ?), avec règles précises (jamais scale(0), jamais animer les raccourcis clavier).
- *shadcn* : conventions strictes de composition (FieldGroup, Item dans Group, tokens sémantiques) pour un code shadcn rigoureux.
- *adapt* : distinguer adaptation (repenser l'expérience par device) et simple mise à l'échelle.
- *better-interface* : revue croisée multi-disciplines (accessibilité, layout, écriture, typo, couleurs) avec échelle de sévérité commune et escalade automatique en HIGH.
- *interaction-design* : timing (100-500ms) et easing standardisés pour microinteractions et transitions.

Ensemble, ces skills forment une boîte à outils de gouvernance granulaire — chacune contraint un aspect précis plutôt que l'ensemble du projet comme DESIGN.md, mais partage la même philosophie : discipliner la génération IA par des règles explicites, contextuelles et vérifiables, plutôt que de la laisser dériver vers des patterns génériques.

À l'opposé, le concept d'**interface générative** ("GUI streamé par un modèle") imagine une UI composée non plus d'éléments GUI traditionnels mais de pixels générés et streamés en temps réel par un modèle, sans structure de composants fixe, promettant flexibilité et richesse visuelle supérieures aux frameworks classiques.

⚠️ **Contradiction** : DESIGN.md et les UI Skills cherchent tous deux à *contraindre* la génération IA — par des règles de projet stables ou par des grilles d'expertise spécialisées et vérifiables (fichier:ligne, sévérité, WCAG) — alors que l'interface générative envisage un rendu entièrement dynamique et non structuré, où même les composants disparaissent au profit de pixels générés à chaque instant. Deux pôles du design assisté par IA — gouvernance/cohérence vs. fluidité/expérimentation totale — dont la réconciliation reste ouverte.

*Nuance interne* : *frontend-design* (skill) et l'interface générative partagent pourtant un même ennemi — l'uniformisation des rendus IA (clichés visuels vs. composants figés) — mais y répondent en sens inverse : plus de règles explicites d'un côté, plus de liberté de rendu de l'autre.

## Sources

- [10 skills IA pour améliorer instantanément le design d'une UI](../sources/2026/2102265246325047711-10-skills-ui-plus-belles.md)
- [DESIGN.md : le standard de Google pour un langage de design partagé avec l'IA](../sources/2026/2047917199655149791-google-design-md-standard.md)
- [Interface générative : le GUI entier streamé par un modèle](../sources/2026/2046975783324004732-generative-computing-pixels-streamed.md)
