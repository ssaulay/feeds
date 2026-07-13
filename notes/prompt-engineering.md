# prompt-engineering

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Karpathy conseille de demander à son LLM de structurer sa réponse en HTML et de visualiser le fichier généré dans un navigateur, ce qui fonctionne très bien. Il théorise que l'audio est l'input préféré des humains vers l'IA, tandis que le visuel (images/vidéos/animations) est l'output préféré de l'IA vers les humains, car le cerveau dédie une part massive de son traitement à la vision. Il anticipe une progression des formats de sortie : texte brut → markdown → HTML → puis à terme des vidéos/simulations interactives générées par des réseaux de diffusion neuronale.

Marc Andreessen (pmarca) partage un prompt système personnalisé conçu pour obtenir des réponses d'expert direct et sans complaisance. Principes clés : incarner un expert mondial avec un raisonnement explicite étape par étape ; vérifier systématiquement faits, citations, noms et dates pour limiter les hallucinations ; bannir les formules de validation flatteuses ("great question", "you're absolutely right") ; mener avec le contre-argument le plus fort avant de défendre une position ; supprimer les avertissements moraux/éthiques sauf demande explicite ; exprimer des niveaux de confiance explicites (haute/moyenne/faible/inconnue) plutôt que des affirmations vagues ; ne pas s'ancrer sur les chiffres fournis par l'utilisateur mais produire ses propres estimations indépendantes.

Ces deux apports touchent des aspects complémentaires du prompt-engineering : Karpathy se concentre sur le *format de sortie* (structuration visuelle), tandis que pmarca se concentre sur le *ton et la rigueur* de la réponse (fond). Aucune contradiction directe entre les deux à ce stade.

## Sources

- [Demander du HTML plutôt que du texte brut aux LLM améliore la lisibilité](../sources/2026/2053872850101285137-llm-output-html-vision.md)
- [Prompt personnalisé de pmarca pour obtenir des réponses IA expertes, directes et sans complaisance](../sources/2026/2051374498994364529-prompt-custom-expert-sans-filtre.md)
