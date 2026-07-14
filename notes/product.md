# product

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Cette note rassemble des annonces, projets et réflexions liés au développement de produits numériques, sans lien thématique direct entre eux.

**Lancements et annonces**

@adilinthewild célèbre sa première année chez Higgsfield en annonçant ce qu'il considère comme le lancement le plus impressionnant de l'entreprise à ce jour. Le tweet renvoie vers un média (image ou vidéo) non accessible, limitant les détails disponibles sur la nature exacte du produit.

70millimètres.fr est une plateforme gratuite et bénévole qui centralise les catalogues de films disponibles sur les services de streaming légal français (Arte, France TV, etc.). Sans publicité, le site est maintenu par des passionnés et propose des sélections, des classiques et des articles pour aider les utilisateurs à trouver quoi regarder légalement. Le modèle est associatif, financé par des dons volontaires (KissKissBankBank), et une section « Ils nous quittent bientôt » signale les films sur le point d'être retirés des plateformes.

**Culture produit et méthodes de développement**

Cat Wu, Head of Product de Claude Code chez Anthropic, décrit comment l'équipe est passée de cycles produit de six mois à des cycles pouvant descendre à un jour, grâce aux research previews et à un « launch room » permanent. Le rôle de PM évolue : il ne s'agit plus de coordonner des roadmaps trimestrielles mais d'habiliter des expéditions quotidiennes. Les rôles PM/ingénieur/designer fusionnent autour de la notion de « goût produit » — l'unité de production la plus efficace étant un ingénieur doté de ce goût, sans PM intermédiaire.

Principes clés de cette culture de shipping rapide :
- Construire des produits à la limite du fonctionnel pour tester immédiatement chaque nouveau modèle et éviter d'accuser un cycle de retard.
- Demander au modèle d'introspecter sur ses propres erreurs pour révéler les failles du prompt système ou du harnais.
- Auditer systématiquement le prompt système à chaque nouveau modèle afin de retirer les béquilles devenues inutiles (dette technique).
- Construire ses propres outils internes (Claude Code, Cowork, Slack) plutôt que d'acheter du SaaS.
- Considérer la personnalité du produit (low-ego, positive, earnest pour Claude) comme un facteur de succès à part entière, non un détail cosmétique.
- Anticiper un futur du travail centré sur la gestion de flottes d'agents IA (50-100 tâches simultanées) plutôt que sur l'exécution directe.
- Recruter des personnes qui accueillent le chaos avec optimisme, condition jugée essentielle face à l'accélération du rythme de l'IA.

**Critique de l'expérience utilisateur moderne**

Un rant satirique dresse un portrait cynique de la dégradation de la tech grand public : publicités omniprésentes, IA imposée partout, friction d'authentification absurde (2FA, tokens de mot de passe bannis), fatigue d'abonnements empilés (abonnement + membership + pourboire, illisibles pour l'utilisateur), mises à jour forcées qui cassent les appareils, et fuites de données récurrentes. L'accumulation de ces frictions, même si chacune paraît justifiable isolément, produit une expérience globalement hostile. Le message central : le « progrès » technologique (IA, updates forcées) est souvent vécu comme une dégradation par l'utilisateur final, pas une amélioration — les dark patterns érodant progressivement la confiance envers les produits.

⚠️ Contradiction : la culture de shipping rapide décrite par Cat Wu (Anthropic) valorise les mises à jour fréquentes, les produits « à la limite du fonctionnel » et l'itération continue comme moteurs de progrès produit. Le rant satirique dénonce au contraire les mises à jour forcées et les produits imposés comme sources de dégradation de l'expérience utilisateur. Ces deux perspectives illustrent une tension non résolue entre vitesse d'innovation côté producteur et stabilité/confort attendus côté utilisateur final.

## Sources

- [Annonce d'un an chez Higgsfield et lancement d'un produit majeur](../sources/2026/2074564269207916984-higgsfield-un-an-lancement.md)
- [70millimètres.fr : moteur de recherche des films disponibles sur les plateformes de streaming légal françaises](../sources/2026/2051228453995745335-70mm-catalogue-streaming-legal.md)
- [Rant satirique sur la dégradation de l'expérience utilisateur moderne](../sources/2026/2049844370203939149-rant-dystopie-tech-moderne.md)
- [Comment l'équipe Claude Code d'Anthropic ship vite : leçons de Cat Wu](../sources/2026/2047669259380383955-claude-code-shipping-culture.md)
