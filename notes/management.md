# management

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

**Adoption de l'IA dans les organisations**

Un post évoque une méthode (média non accessible) jugée efficace pour accélérer l'adoption de l'IA dans les départements non-techniques, sans détailler son contenu.

Un second apport propose une méthode concrète et documentée : plutôt qu'un mandat top-down déclarant l'IA "le travail de tout le monde" (donc de personne), une CPO recrute une personne dédiée — un "Sasha" — chargée d'automatiser, fonction par fonction, le workflow le plus fastidieux. Le succès visible d'un premier cas d'usage (ex. briefing automatisé pour le customer success) génère une demande organique des autres équipes, qui tirent la transformation au lieu qu'elle soit imposée. Ce rôle est vu comme l'évolution du BizOps généraliste vers un "AI Ops" dont l'objectif est de transformer l'edge d'un top performer en plancher de compétence pour toute l'entreprise.

Un troisième apport détaille une approche complémentaire orientée infrastructure : un PM investit 30 jours pour bâtir un "Team OS" — un dépôt partagé dans Claude Code — permettant ensuite à 20+ personnes de s'auto-servir sans passer par lui. La clé consiste à checker dans le repo toutes les métriques, requêtes SQL, schémas de tables et dashboards, et à en faire une condition obligatoire au lancement de chaque feature ; cela élimine le rôle de routeur humain pour les données et empêche le système de se dégrader avec le temps. L'effet est cumulatif : chaque sprint automatise une tâche de plus, libérant du temps pour la suivante, creusant un écart croissant avec les équipes qui n'adoptent pas cette approche. La vraie leverage de l'IA ne serait donc pas la productivité individuelle mais un repo partagé traversable par toute l'équipe — la barrière à l'adoption étant surtout psychologique (peur du terminal) plutôt que technique.

Les trois apports convergent : que ce soit via un rôle dédié (Sasha) ou une infrastructure partagée (Team OS), l'enjeu est de sortir d'un mandat descendant flou pour créer un système concret — personne ou repo — qui absorbe le travail répétitif et devient le point d'appui organique de l'adoption de l'IA par le reste de l'équipe.

**Développer l'autonomie et l'agentivité des employés**

Un framework (crédité à @stephsmithio) décrit 5 niveaux de contribution face à un problème : signaler, diagnostiquer, proposer des solutions, recommander une solution, puis agir en autonomie. L'auteur l'utilise avec chaque nouvel employé en fixant l'attente de démarrer directement au niveau 4 (problème + causes + solutions + recommandation) plutôt que de se contenter de remonter des problèmes bruts. Le niveau 5 (identifier, résoudre et informer après coup) se gagne progressivement, à mesure que la confiance s'établit avec le management. Le fait d'être "high agency" n'est pas ponctuel : cela doit imprégner toute la manière de travailler d'un employé.

Ce framework résonne avec les approches "Sasha" et "Team OS" décrites ci-dessus : dans les trois cas, l'enjeu est de responsabiliser un individu, une fonction ou une infrastructure pour qu'ils agissent et permettent l'auto-service, plutôt que d'attendre une impulsion ou un mandat descendant — que ce soit pour piloter l'adoption de l'IA ou pour traiter un problème métier.

## Sources

- [Une méthode efficace pour accélérer l'adoption de l'IA dans les équipes non-techniques](../sources/2026/2074666373402464442-methode-adoption-ia-non-tech.md)
- [La stratégie AI qui marche : embaucher un 'Sasha' plutôt qu'un mandat top-down](../sources/2026/2072048527996604900-embaucher-son-sasha-ai-ops.md)
- [Les 5 niveaux de travail pour former des employés à haute agentivité](../sources/2026/2070194343034360004-5-niveaux-de-travail-agency.md)
- [Construire un 'Team OS' dans Claude Code pour scaler une équipe entière](../sources/2026/2044520404094759185-team-os-claude-code.md)
