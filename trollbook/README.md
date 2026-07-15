# trollbook

[Lien vers Kattis](https://open.kattis.com/problems/trollbook)

Thème : Structures de données (dictionnaire)

## Résumé

Étant donné `n` paires (mot, numéro de page), reconstruire et afficher la phrase formée par les mots dans l'ordre croissant de leur numéro de page.

## Idée

Stocker chaque mot dans un dictionnaire indexé par son numéro de page (`book[page] = word`), puis reconstruire la phrase en itérant sur les numéros de page de 1 à `n` et en récupérant le mot associé à chacun.

Ça fonctionne parce que le dictionnaire inverse directement la relation donnée en entrée (mot → page) en la relation dont on a besoin pour la sortie (page → mot), avec un accès O(1) par page. C'est plus direct que de stocker les paires dans une liste puis de la trier par page : on connaît déjà l'ensemble exact des clés recherchées (`1` à `n`), donc un dictionnaire avec accès direct évite le coût d'un tri.

## Algorithme

1. Lire `n`.
2. Pour chaque paire, lire le mot et son numéro de page, et les stocker dans `book[page] = mot`.
3. Construire la phrase en récupérant `book[i]` pour `i` de `1` à `n`.
4. Afficher la phrase, mots séparés par des espaces.

## Complexité

- Temps : O(n) pour la lecture et la reconstruction.
- Mémoire : O(n) pour le dictionnaire.

## Difficultés rencontrées

Le code suppose que les numéros de page couvrent exactement `1` à `n` sans trou ni doublon ; si une page manquait, `book[i]` lèverait une `KeyError`. C'est garanti par l'énoncé de ce problème, mais c'est une hypothèse à vérifier avant de réutiliser ce pattern ailleurs.

## Ce que j'ai appris

- Trier explicitement (`sorted(pairs, key=...)`) n'est pas toujours nécessaire : quand les clés cibles sont un ensemble connu et dense (ici `1..n`), un dictionnaire avec accès direct par clé est plus simple et tout aussi efficace, sans le coût O(n log n) d'un tri.

## Améliorations possibles

Aucune : la solution est déjà linéaire, ce qui est optimal pour ce problème (il faut au minimum lire toutes les entrées).
