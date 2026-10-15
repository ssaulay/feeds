# design

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Quatre apports dessinent un paysage du design assisté (ou non) par IA organisé autour d'un axe central : gouvernance/règles explicites vs. fluidité/génération libre — complété par un troisième pôle, la curation humaine de références réelles.

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

**mkdir.directory** introduit un troisième pôle, en amont de toute génération : un annuaire curé de 31 répertoires d'inspiration design web (Awwwards, Siteinspire, Land-book, The FWA, Save.design...), gratuit et sans compte, avec un système de vote par usage réel qui réordonne les résultats. Sa logique n'est ni la règle encodée ni la génération libre, mais la curation humaine de références existantes comme point de départ de conception — volontairement limitée (31 entrées) pour éviter la surcharge de choix.

⚠️ **Contradiction** : DESIGN.md et les UI Skills cherchent tous deux à *contraindre* la génération IA — par des règles de projet stables ou par des grilles d'expertise spécialisées et vérifiables (fichier:ligne, sévérité, WCAG) — alors que l'interface générative envisage un rendu entièrement dynamique et non structuré, où même les composants disparaissent au profit de pixels générés à chaque instant. Deux pôles du design assisté par IA — gouvernance/cohérence vs. fluidité/expérimentation totale — dont la réconciliation reste ouverte.

*Nuance interne* : *frontend-design* (skill) et l'interface générative partagent pourtant un même ennemi — l'uniformisation des rendus IA (clichés visuels vs. composants figés) — mais y répondent en sens inverse : plus de règles explicites d'un côté, plus de liberté de rendu de l'autre.

*Nuance ajoutée* : mkdir.directory vise le même ennemi — le générique — via une troisième voie, antérieure aux deux autres : au lieu d'encoder des règles (DESIGN.md, UI Skills) ou de laisser un modèle générer librement (interface générative), on s'inspire de réalisations humaines éprouvées et votées par la pratique. C'est un complément plutôt qu'une contradiction : la curation nourrit en amont les règles qu'un DESIGN.md ou un skill *frontend-design* viendront ensuite formaliser et vérifier.

## Sources

- [mkdir.directory - Annuaire curé de sites d'inspiration design](../sources/2026/2110122317384687749-annuaire-inspiration-design-web.md)
- [10 skills IA pour améliorer instantanément le design d'une UI](../sources/2026/2102265246325047711-10-skills-ui-plus-belles.md)
- [DESIGN.md : le standard de Google pour un langage de design partagé avec l'IA](../sources/2026/2047917199655149791-google-design-md-standard.md)
- [Interface générative : le GUI entier streamé par un modèle](../sources/2026/2046975783324004732-generative-computing-pixels-streamed.md)
