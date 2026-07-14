# dev-tools

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Cette note couvre des outils facilitant différentes étapes du cycle de vie d'un projet dev, du déploiement à la communication, en passant par l'optimisation des workflows IA.

**Déploiement** : Vercel Drop permet de déployer un fichier ou dossier en le glissant directement dans le navigateur, sans Git ni CLI. L'outil détecte automatiquement les frameworks (Next.js) ou déploie des sites statiques tels quels, générant une URL de production en quelques secondes.

**Communication / marketing produit** : le skill Claude Code `/brag` génère automatiquement une vidéo de lancement (~20 secondes, musique, animations, effets sonores) à partir d'un simple prompt ("/brag about this"), pour n'importe quel side project. Il s'appuie sur HyperFrames, le moteur open-source HTML-to-video de HeyGen, propose plusieurs presets de style et génère aussi le copy prêt à partager. L'outil vise à remplacer les posts de lancement peu engageants (simples screenshots statiques) par un format vidéo professionnel. Gratuit, open source, avec des démos incluses pour tester sans projet réel.

**Optimisation des workflows IA / gestion du contexte** : une astuce propose de connecter Claude Code à NotebookLM pour utiliser ce dernier comme couche de mémoire/contexte externe, plutôt que de tout faire transiter par le contexte du LLM. L'objectif serait d'économiser des tokens et de prolonger la durée effective des sessions de codage assisté par IA. Cette approche s'inscrit dans une tendance plus large d'orchestration d'outils IA complémentaires pour contourner les limites de contexte des LLM. À noter : la source reste très synthétique, sans détail technique précis sur l'implémentation concrète (comment NotebookLM s'interface avec Claude Code, quel protocole ou quelle API est utilisé).

## Sources

- [/brag : générer automatiquement une vidéo de lancement depuis Claude Code](../sources/2026/2069039170451091878-brag-skill-claude-code-video.md)
- [Vercel Drop : déployer un site en glissant un dossier dans le navigateur](../sources/2026/2065492873555100098-vercel-drop-deploy-drag-drop.md)
- [Connecter Claude Code à NotebookLM pour économiser des tokens et prolonger les sessions](../sources/2026/2042295647362019800-claude-code-notebooklm-tokens.md)
