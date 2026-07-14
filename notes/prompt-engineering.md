# prompt-engineering

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Karpathy conseille de demander à son LLM de structurer sa réponse en HTML et de visualiser le fichier généré dans un navigateur, ce qui fonctionne très bien. Il théorise que l'audio est l'input préféré des humains vers l'IA, tandis que le visuel (images/vidéos/animations) est l'output préféré de l'IA vers les humains, car le cerveau dédie une part massive de son traitement à la vision. Il anticipe une progression des formats de sortie : texte brut → markdown → HTML → puis à terme des vidéos/simulations interactives générées par des réseaux de diffusion neuronale.

Marc Andreessen (pmarca) partage un prompt système personnalisé conçu pour obtenir des réponses d'expert direct et sans complaisance. Principes clés : incarner un expert mondial avec un raisonnement explicite étape par étape ; vérifier systématiquement faits, citations, noms et dates pour limiter les hallucinations ; bannir les formules de validation flatteuses ("great question", "you're absolutely right") ; mener avec le contre-argument le plus fort avant de défendre une position ; supprimer les avertissements moraux/éthiques sauf demande explicite ; exprimer des niveaux de confiance explicites (haute/moyenne/faible/inconnue) plutôt que des affirmations vagues ; ne pas s'ancrer sur les chiffres fournis par l'utilisateur mais produire ses propres estimations indépendantes.

Un troisième apport aborde le prompt-engineering appliqué à l'implémentation de specs par des agents IA : maintenir en continu un fichier `implementation-notes.html` documentant décisions de design, déviations, compromis et questions ouvertes. Le constat de départ est qu'aucune spec n'est jamais totalement exhaustive — il reste toujours des zones grises que l'agent doit trancher en cours de route. Plutôt que d'exiger une conformité stricte impossible, ce prompt donne explicitement à l'agent la permission de prendre des décisions, ce qui produit de meilleurs résultats. Le fichier sert à la fois de trace d'audit et de point de synchronisation asynchrone entre l'humain et l'agent, sans bloquer le flux de travail.

Ces trois apports touchent des facettes complémentaires du prompt-engineering : Karpathy se concentre sur le *format de sortie* (structuration visuelle, réutilisé ici via le choix du HTML pour le fichier de notes), pmarca sur le *ton et la rigueur* de la réponse (fond), et le troisième sur la *gestion de l'autonomie de l'agent* dans des tâches longues et sous-spécifiées. On note un point de convergence intéressant : le choix du format HTML (Karpathy) réapparaît ici comme support concret pour le fichier `implementation-notes.html`, suggérant que le HTML s'impose comme format pivot pour les échanges humain-IA, que ce soit en réponse ponctuelle ou en documentation continue. Aucune contradiction directe entre ces trois apports.

Un quatrième apport annonce un atelier vidéo de 24 minutes par l'équipe Anthropic, présenté comme révélant des techniques avancées pour prompter Claude. Cependant, le contenu réel de l'atelier et du guide mentionné n'est pas accessible (seul un tweet cité sans détail est disponible). Le format et le ton du post — urgence, superlatifs, comparaison à des cours payants — sont typiques du marketing viral sur X plutôt que d'un partage de savoir vérifié. Ce quatrième apport n'ajoute donc aucune substance exploitable au corpus : il ne peut être ni comparé ni intégré aux principes concrets dégagés par les trois premiers apports, faute de contenu vérifiable.

## Sources

- [Maintenir un fichier implementation-notes.html pour combler les ambiguïtés de spec avec un agent IA](../sources/2026/2056418157305454805-implementation-notes-file-spec.md)
- [Demander du HTML plutôt que du texte brut aux LLM améliore la lisibilité](../sources/2026/2053872850101285137-llm-output-html-vision.md)
- [Prompt personnalisé de pmarca pour obtenir des réponses IA expertes, directes et sans complaisance](../sources/2026/2051374498994364529-prompt-custom-expert-sans-filtre.md)
- [Annonce d'un atelier Anthropic sur le prompting de Claude (contenu non accessible)](../sources/2026/2048418646960288059-atelier-anthropic-prompt-claude.md)
