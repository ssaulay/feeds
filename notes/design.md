# design

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Deux approches émergent pour penser le design dans les workflows IA, à des niveaux presque opposés.

**DESIGN.md** est un format markdown proposé par Google pour encoder les règles de design (couleurs, typographie, spacing, composants) de façon portable entre outils (Stitch, agents de code, builders). L'objectif : une mémoire de projet réutilisable qui garde la cohérence visuelle tout au long du workflow, de l'exploration initiale jusqu'à l'implémentation finale, en servant de garde-fou pour les agents IA. Cette approche mise sur des règles explicites et stables pour discipliner la génération.

À l'opposé, le concept d'**interface générative** ("GUI streamé par un modèle") imagine une UI qui ne serait plus composée d'éléments GUI traditionnels mais de pixels générés et streamés en temps réel par un modèle. Plutôt que d'assembler des composants pré-définis, le rendu visuel serait entièrement piloté par l'IA à la volée, promettant une flexibilité et une richesse visuelle supérieures aux frameworks UI classiques. Ce concept pousse la logique du generative UI au-delà des composants, vers un rendu sans structure fixe.

⚠️ Contradiction (implicite) : DESIGN.md cherche à *contraindre* la génération IA par des règles stables garantissant la cohérence visuelle, tandis que l'interface générative envisage un rendu entièrement dynamique et non structuré, où même les composants disparaissent au profit de pixels générés à chaque instant. Les deux visions coexistent comme deux pôles du design assisté par IA : gouvernance/cohérence vs. fluidité/expérimentation totale — reste à voir comment (ou si) elles peuvent se réconcilier.

## Sources

- [DESIGN.md : le standard de Google pour un langage de design partagé avec l'IA](../sources/2026/2047917199655149791-google-design-md-standard.md)
- [Interface générative : le GUI entier streamé par un modèle](../sources/2026/2046975783324004732-generative-computing-pixels-streamed.md)
