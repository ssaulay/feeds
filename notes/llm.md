# llm

*Note de synthèse vivante — mise à jour automatiquement à chaque nouvel apport.*

## Synthèse

Le RAG basique (naive RAG) souffre de plusieurs limites : faible rappel, hallucinations, perte du contexte au milieu des documents, manque de connaissance de domaine. Le RAG avancé corrige ces problèmes à trois niveaux : avant la récupération (chunking, self-query, densification via LLM), pendant (hybrid search, multi-stage, graph RAG, multi-hop) et après (re-ranking, compression contextuelle, corrective RAG, vérification des citations, context fusion). L'article évoque aussi les tendances futures vers des systèmes agentiques et multimodaux, orchestrables via n8n.

Sur le volet multimodal, Google concrétise cette tendance avec **Gemini Embedding 2**, un modèle d'embedding nativement multimodal qui unifie texte, image, vidéo (jusqu'à 2 min), audio natif et PDF dans un seul espace vectoriel de 3072 dimensions. Il remplace les pipelines historiques à plusieurs modèles (CLIP pour l'image, Whisper pour l'audio, un embedder texte séparé) qu'il fallait aligner manuellement — une simplification architecturale directement pertinente pour le RAG avancé multimodal évoqué ci-dessus. Points clés :

- **Un seul espace vectoriel** remplace les stacks multi-modèles, avec des gains mesurés : 68.32 sur MTEB, -70% de latence chez Sparkonomy.
- **Audio natif** : encodage direct sans transcription intermédiaire, permettant d'indexer des podcasts dans le même espace que du texte.
- **Recherche cross-modale** (texte + image simultanément) sans avoir à stitcher plusieurs vector stores.
- **Matryoshka Representation Learning** : troncation du vecteur de 3072 à 768 dimensions sans perte de qualité, divisant le stockage par 4.
- **Prix compétitif** : 0.20$/M tokens (0.10$ en batch), rendant l'indexation à grande échelle abordable.
- Lecture stratégique : Google construit des briques d'infrastructure qui rendent obsolètes plusieurs produits concurrents à la fois (CLIP, Whisper, embedders spécialisés), pendant que la concurrence communique surtout via des démos.

Toujours sur le multimodal, mais côté génération (et non plus embedding) : **Miso One** est un modèle text-to-speech open source de 8 milliards de paramètres, atteignant 110ms de latence — plus rapide qu'un temps de réponse humain typique — pour une parole décrite comme la plus expressive/émotive au monde en synthèse vocale. Les poids sont déjà disponibles, l'API arrivant prochainement. Ce cas illustre qu'une miniaturisation relative (8B) suffit à obtenir une expressivité élevée, et complète la tendance audio native déjà notée avec Gemini Embedding 2 : d'un côté l'indexation/compréhension de l'audio (embedding), de l'autre sa génération quasi indiscernable d'une voix humaine — deux briques qui, combinées, rapprochent les agents vocaux temps réel de l'interaction humaine naturelle.

Sur le volet pédagogique, une vidéo de 2h d'**Andrej Karpathy** (co-fondateur d'OpenAI) sur l'utilisation pratique des LLMs circule comme référence, présentée comme plus formatrice que les tutoriels IA habituels. Ce bookmark reste toutefois un pointeur incomplet : ni transcript ni description détaillée du contenu ne sont disponibles pour l'instant. À compléter/vérifier dès qu'une source donne accès au contenu réel (thèmes abordés, recommandations concrètes) pour l'intégrer utilement à la synthèse — actuellement, la seule information exploitable est le signal de recommandation (autorité de l'auteur + format long conseillé pour un visionnage approfondi plutôt qu'un survol).

Dans une veine pédagogique complémentaire mais plus pratique, **Felix Rieseberg** propose un manuel interactif pour construire soi-même un modèle de langage, accessible sans expérience de programmation ni de machine learning. Contrairement au format vidéo passif de Karpathy, l'outil mise sur des playgrounds intégrés permettant de manipuler directement tokenizer, embeddings, attention et courbes d'entraînement — deux approches (vidéo longue vs. textbook interactif manipulable) qui se complètent pour démystifier le fonctionnement interne des LLMs plutôt que leur seul usage. Points clés :

- Le contenu vise explicitement les non-programmeurs, avec des approfondissements optionnels pour les curieux souhaitant aller plus loin.
- L'exemple pratique reprend une recette type **nanoGPT** (25M paramètres) entraînée sur le dataset **TinyStories**, avec warmup linéaire puis décroissance cosinus du learning rate.
- Détail technique notable : **AdamW** n'est appliqué qu'aux poids de multiplication matricielle, en excluant RMSNorm et les embeddings de la régularisation.
- L'objectif est de rendre tangible l'évolution de la loss curve et de la qualité du texte généré au fil des checkpoints, plutôt que de rester sur une explication théorique abstraite.
- Ce projet illustre une tendance plus large : démocratiser la compréhension du pré-entraînement (jusqu'ici perçu comme réservé aux experts) via des interfaces manipulables, en écho à la simplification architecturale déjà observée côté infrastructure (Gemini Embedding 2) et côté génération (Miso One).

## Sources

- [Un manuel interactif pour construire son propre modèle de langage](../sources/2026/2079624265528475975-build-your-own-language-model.md)
- [Techniques avancées de RAG pour des systèmes de récupération fiables en production](../sources/2026/2065403846940147866-advanced-rag-techniques-guide.md)
- [Miso One : un modèle text-to-speech ultra-expressif en open source](../sources/2026/2062269826177868211-miso-one-voice-model.md)
- [Gemini Embedding 2 : un seul espace vectoriel pour texte, image, audio, vidéo et PDF](../sources/2026/2047003304937332860-gemini-embedding-2-multimodal.md)
- [Vidéo de 2h par Andrej Karpathy sur l'utilisation des LLMs](../sources/2026/2046612983007039794-karpathy-video-llm-usage.md)
