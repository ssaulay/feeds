# product

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Cette note rassemble des annonces, projets et réflexions liés au développement de produits numériques, sans lien thématique direct entre eux.

**Lancements et annonces**

@adilinthewild célèbre sa première année chez Higgsfield en annonçant ce qu'il considère comme le lancement le plus impressionnant de l'entreprise à ce jour. Le tweet renvoie vers un média (image ou vidéo) non accessible, limitant les détails disponibles sur la nature exacte du produit.

70millimètres.fr est une plateforme gratuite et bénévole qui centralise les catalogues de films disponibles sur les services de streaming légal français (Arte, France TV, etc.). Sans publicité, le site est maintenu par des passionnés et propose des sélections, des classiques et des articles pour aider les utilisateurs à trouver quoi regarder légalement. Le modèle est associatif, financé par des dons volontaires (KissKissBankBank), et une section « Ils nous quittent bientôt » signale les films sur le point d'être retirés des plateformes.

Une nouvelle fonctionnalité « Automations » propose trois façons de construire des workflows : éditeur visuel drag-and-drop, langage naturel piloté par IA, ou code direct via des outils comme Claude Code, Cursor ou Codex. Cette approche hybride vise à toucher différents profils d'utilisateurs (du non-technique au développeur) en offrant plusieurs niveaux d'abstraction pour une même fonctionnalité, et se positionne explicitement en opposition aux outils « old-school » de marketing automation — une stratégie de différenciation produit. L'intégration d'outils de codage IA dans un SaaS grand public illustre la convergence croissante entre no-code et développement assisté par IA, et fait écho à la place centrale que prend Claude Code comme brique d'infrastructure produit (cf. section suivante).

**Culture produit et méthodes de développement (Anthropic / Claude Code)**

Cat Wu, Head of Product de Claude Code chez Anthropic, décrit à plusieurs reprises comment l'équipe est passée de cycles produit de six mois à des cycles de semaines, puis de jours seulement, grâce aux research previews et à un « launch room » permanent. Le rôle de PM évolue en profondeur : il ne s'agit plus de coordonner des roadmaps trimestrielles mais d'habiliter des expéditions quotidiennes. Les rôles PM/ingénieur/designer fusionnent autour de la notion de « goût produit » — l'unité de production la plus efficace étant un ingénieur doté de ce goût, sans PM intermédiaire.

Principes clés de cette culture de shipping rapide :
- Construire des produits à la limite du fonctionnel — voire qui ne fonctionnent pas encore — en pariant sur les futurs modèles pour tester immédiatement chaque nouvelle capacité et éviter d'accuser un cycle de retard.
- Une automatisation à 95% n'est pas vraiment une automatisation utilisable : viser le seuil de fiabilité qui rend le produit réellement exploitable, pas une démonstration partielle.
- Demander au modèle d'introspecter sur ses propres erreurs pour révéler les failles du prompt système ou du harnais ; l'introspection IA est une compétence sous-estimée mais clé pour les PMs eux-mêmes.
- Auditer systématiquement le prompt système à chaque nouveau modèle afin de retirer les béquilles devenues inutiles (dette technique).
- Construire ses propres outils internes (Claude Code, Cowork, Slack) plutôt que d'acheter du SaaS.
- Considérer la personnalité du produit (low-ego, positive, earnest pour Claude) comme un facteur de succès à part entière, non un détail cosmétique.
- Anticiper un futur du travail centré sur la gestion de flottes d'agents IA (50-100 tâches simultanées) plutôt que sur l'exécution directe.
- Recruter des personnes qui accueillent le chaos avec optimisme et privilégier des compétences PM différentes des compétences traditionnelles — être « AGI-pilled » au bon dosage aidant à anticiper les capacités futures des modèles plutôt qu'à concevoir pour les limites actuelles.

À noter : Claude Code, présenté ici comme un outil interne construit en interne plutôt qu'acheté (« build vs. buy »), apparaît par ailleurs intégré comme brique externe dans des produits SaaS tiers (cf. « Automations » ci-dessus) — signe que l'écosystème des outils de codage IA devient une infrastructure standard, à la fois interne et externe, pour construire des produits.

**Mesurer la qualité des produits IA : les AI evals (Teresa Torres)**

Teresa Torres explique pourquoi les équipes produit — pas seulement les ingénieurs — doivent apprendre à construire des « AI evals ». Contrairement au code traditionnel, les LLM sont probabilistes : une même entrée peut produire des sorties différentes, et leurs réponses sémantiques échappent au jugement binaire des tests unitaires classiques. Il faut donc définir explicitement ce à quoi ressemble une « bonne réponse » — un travail sémantique dépendant du contexte produit, qui ne peut pas être sous-traité à un vendor d'outils d'eval.

Méthode en deux étapes :
1. **Analyse d'erreur** : lire en détail les traces de sorties LLM sur des cas réels et catégoriser les types d'erreurs. Une analyse légère sur peu d'exemples suffit pour des workflows personnels ; les produits customer-facing exigent l'analyse de centaines de traces réelles.
2. **Choix du type d'eval** pour mesurer la fréquence de ces erreurs, parmi quatre types : golden dataset (tâches simples à réponse unique), code assertion (rapide, déterministe), LLM-as-a-judge (qualité sémantique, mais coûteux) et feedback client.

Pour un LLM-as-a-judge efficace : donner une tâche plus simple que l'originale, exiger une réponse binaire, aligner le juge sur un jugement humain de référence, et accepter qu'il produira lui aussi des erreurs.

Ce guide fait écho au principe de Cat Wu selon lequel « une automatisation à 95% n'est pas vraiment utilisable » : les evals fournissent précisément la méthode pour mesurer ce taux de réussite et déterminer objectivement où se situe le seuil de fiabilité exploitable — reliant la culture de shipping rapide d'Anthropic à une pratique concrète de mesure de qualité, désormais présentée comme une compétence PM à part entière au même titre que l'introspection IA.

**Critique de l'expérience utilisateur moderne**

Un rant satirique dresse un portrait cynique de la dégradation de la tech grand public : publicités omniprésentes, IA imposée partout, friction d'authentification absurde (2FA, tokens de mot de passe bannis), fatigue d'abonnements empilés (abonnement + membership + pourboire, illisibles pour l'utilisateur), mises à jour forcées qui cassent les appareils, et fuites de données récurrentes. L'accumulation de ces frictions, même si chacune paraît justifiable isolément, produit une expérience globalement hostile. Le message central : le « progrès » technologique (IA, updates forcées) est souvent vécu comme une dégradation par l'utilisateur final, pas une amélioration — les dark patterns érodant progressivement la confiance envers les produits.

⚠️ Contradiction : la culture de shipping rapide décrite par Cat Wu (Anthropic) valorise les mises à jour fréquentes, les produits « à la limite du fonctionnel » (voire non fonctionnels, en pari sur le futur) et l'itération continue comme moteurs de progrès produit. Le rant satirique dénonce au contraire les mises à jour forcées et les produits imposés comme sources de dégradation de l'expérience utilisateur. Ces deux perspectives illustrent une tension non résolue entre vitesse d'innovation côté producteur et stabilité/confort attendus côté utilisateur final. La méthode des AI evals de Teresa Torres offre un début de réponse à cette tension : en exigeant une mesure rigoureuse du taux de réussite avant de considérer une fonctionnalité IA comme exploitable, elle introduit un garde-fou qui pourrait limiter les dérives dénoncées par le rant tout en préservant la vitesse d'itération.

## Sources

- [Guide pratique des AI evals pour les équipes produit](../sources/2026/2095634825931866181-guide-evals-ia-product-teams.md)
- [70millimètres.fr : moteur de recherche des films disponibles sur les plateformes de streaming légal françaises](../sources/2026/2051228453995745335-70mm-catalogue-streaming-legal.md)
- [Rant satirique sur la dégradation de l'expérience utilisateur moderne](../sources/2026/2049844370203939149-rant-dystopie-tech-moderne.md)
- [Comment l'équipe Claude Code d'Anthropic ship vite : leçons de Cat Wu](../sources/2026/2047669259380383955-claude-code-shipping-culture.md)
- [Comment l'équipe produit d'Anthropic (Claude Code) shippe à une vitesse inédite](../sources/2026/2047377335406694431-anthropic-product-team-shipping-pace.md)
- [Lancement d'Automations : workflows via drag-and-drop, IA ou code (Claude Code, Cursor, Codex)](../sources/2026/2043695848790589741-automations-drag-drop-ai-code.md)
