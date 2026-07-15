# grading

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `Grading`)*

Thème : Implémentation

## Résumé

Étant donné cinq seuils de notes (du plus haut au plus bas) et un score d'examen, afficher la lettre correspondante (A à F).

## Idée

Comparer le score aux seuils dans l'ordre décroissant avec une chaîne de `if/elif`, en retournant la première lettre dont le seuil est atteint.

Ça fonctionne parce que les seuils sont fournis du plus exigeant au moins exigeant : dès que `examScore >= seuil`, c'est la meilleure lettre possible, donc tester dans cet ordre et s'arrêter au premier succès donne directement la bonne réponse.

## Algorithme

1. Lire les cinq seuils `a, b, c, d, e`.
2. Lire le score de l'examen.
3. Tester les seuils du plus haut au plus bas et afficher la première lettre correspondante, ou `F` si aucun seuil n'est atteint.

## Complexité

- Temps : O(1).
- Mémoire : O(1).

## Difficultés rencontrées

L'ordre des seuils est essentiel : le code suppose `a >= b >= c >= d >= e`. Si l'énoncé donnait les seuils dans un autre ordre, la logique `if/elif` serait fausse.

## Ce que j'ai appris

- Une chaîne de `if/elif` ordonnée est la façon la plus directe de traiter des seuils imbriqués, plus lisible qu'une recherche dans une liste de tuples pour seulement cinq cas.

## Améliorations possibles

Pour un nombre de seuils variable, une boucle sur une liste `[(a, "A"), (b, "B"), ...]` généraliserait la logique sans dupliquer de code.
