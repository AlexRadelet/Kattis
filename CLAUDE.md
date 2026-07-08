# CLAUDE.md

## Contexte

Ce dépôt contient mes solutions aux problèmes du site Kattis.

L'objectif n'est pas seulement d'archiver du code, mais de constituer une bibliothèque personnelle de
résolution de problèmes, d'algorithmes et de techniques.

Le dépôt doit rester cohérent dans le temps.

## Langage

- Python 3 uniquement.
- Le code doit rester compatible avec l'environnement de soumission de Kattis.
- Pas de dépendances externes.

## Organisation du dépôt

Chaque problème possède son propre dossier.

```
category/
└── problem_name/
    ├── solution.py
    ├── README.md
    └── sample_input.txt (optionnel)
```

Les catégories correspondent au principal thème algorithmique :

- implementation
- math
- greedy
- graphs
- dynamic_programming
- strings
- sorting
- searching
- data_structures
- geometry
- simulation
- miscellaneous

Si un problème appartient à plusieurs catégories, choisir celle qui représente le concept principal utilisé
pour la solution.

## solution.py

Le fichier `solution.py` doit contenir uniquement la solution destinée à être soumise sur Kattis.

Éviter :

- les commentaires inutiles ;
- le code mort ;
- les impressions de débogage ;
- les fonctions non utilisées.

Le code doit privilégier :

- la lisibilité ;
- des noms de variables explicites ;
- une complexité optimale lorsque cela est raisonnable.

## README.md

Chaque problème possède un README suivant exactement cette structure.

### Nom du problème

Lien vers Kattis

### Résumé

Une phrase expliquant ce que demande le problème.

### Idée

Expliquer l'approche choisie.

Pourquoi fonctionne-t-elle ?

Pourquoi ce choix plutôt qu'un autre ?

### Algorithme

Décrire les principales étapes.

### Complexité

- Temps :
- Mémoire :

### Difficultés rencontrées

Lister les erreurs, pièges ou mauvaises pistes rencontrés pendant la résolution.

Même si elles semblent évidentes après coup.

### Ce que j'ai appris

Noter les notions importantes retenues.

Par exemple :

- une propriété mathématique ;
- une structure de données ;
- une technique Python ;
- un piège du problème.

### Améliorations possibles

Décrire une solution plus élégante ou plus performante si elle existe.

## Règles de rédaction

Les explications doivent être :

- rédigées en français ;
- concises mais complètes ;
- destinées à mon futur moi dans plusieurs mois.

Éviter les explications vagues.

Toujours expliquer **pourquoi** une solution fonctionne, pas uniquement **ce qu'elle fait**.

## Lorsque je demande de documenter un problème

Claude doit :

1. Lire mon code.
2. Ne jamais modifier l'algorithme sans me le proposer explicitement.
3. Identifier le thème algorithmique principal.
4. Générer le README complet.
5. Donner la complexité temporelle et mémoire.
6. Mentionner les pièges éventuels.
7. Mettre en avant les notions intéressantes à retenir.

## Lorsque je demande une revue de code

Claude doit :

- rechercher des simplifications ;
- vérifier la complexité ;
- signaler les cas limites ;
- proposer des améliorations de lisibilité ;
- ne jamais sacrifier la clarté pour gagner quelques lignes.

## Style Python

Privilégier :

- les compréhensions lorsqu'elles améliorent réellement la lisibilité ;
- les fonctions lorsque cela clarifie le code ;
- les noms explicites.

Éviter les astuces ("code golf") qui rendent le code difficile à comprendre.

## Commits Git

Utiliser des messages explicites.

Exemples :

- Add solution for dicecup
- Add explanation for shortestpath1
- Improve documentation for knapsack
- Refactor graph utilities

Ne jamais utiliser :

- Update
- Fix
- Changes

## Objectif long terme

Ce dépôt doit devenir :

- un portfolio montrant ma progression ;
- un carnet de révision pour les entretiens techniques ;
- une bibliothèque d'algorithmes documentés ;
- une référence personnelle sur les problèmes déjà résolus.

Chaque nouvelle contribution doit améliorer la qualité globale du dépôt.
