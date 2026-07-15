# Kattis

Mes solutions aux problèmes du site [Kattis](https://open.kattis.com/).

Ce dépôt n'est pas qu'une archive de code : chaque problème est accompagné d'une explication de l'approche choisie, de sa complexité et des pièges rencontrés. L'objectif est d'en faire :

- un portfolio montrant ma progression ;
- un carnet de révision pour les entretiens techniques ;
- une bibliothèque d'algorithmes documentés ;
- une référence personnelle sur les problèmes déjà résolus.

## Organisation

Chaque problème a son propre dossier à la racine du dépôt, sans regroupement par catégorie :

```
problem_name/
├── solution.py
└── README.md
```

Le thème algorithmique de chaque problème (graphes, math, strings, etc.) est indiqué dans son README (champ **Thème**). Une synthèse de révision organisée par thème, avec les patterns et pièges récurrents observés à travers tous les problèmes, est tenue à jour séparément (Google Doc personnel).

Les règles de contribution (structure des README, style de code, conventions de commit) sont détaillées dans [CLAUDE.md](CLAUDE.md).

Le dossier [data_structures_practice](data_structures_practice) contient des implémentations génériques de structures de données (arbre binaire de recherche, liste chaînée, table de hachage, tas, etc.) réalisées en dehors de Kattis, à titre d'entraînement — il ne suit pas le format problème/solution ci-dessus.
