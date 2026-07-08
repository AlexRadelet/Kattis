# rectangle_area

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `rectangleArea`)*

## Résumé

Étant donné les coordonnées de deux coins opposés d'un rectangle, calculer son aire.

## Idée

Calculer la valeur absolue du produit des différences de coordonnées : `|x2-x1| × |y2-y1|`.

Ça fonctionne parce que l'aire d'un rectangle aligné sur les axes est le produit de sa largeur et de sa hauteur, indépendamment de l'ordre dans lequel les deux coins sont donnés. La valeur absolue évite un résultat négatif si les coordonnées ne sont pas données dans un ordre croissant.

## Algorithme

1. Lire les quatre coordonnées `x1, y1, x2, y2`.
2. Calculer l'aire avec `abs((x2-x1)*(y2-y1))`.
3. Afficher le résultat avec 2 décimales.

## Complexité

- Temps : O(1).
- Mémoire : O(1).

## Difficultés rencontrées

Sans le `abs()`, un rectangle dont les coins sont donnés dans un ordre "inversé" (ex: coin inférieur droit puis coin supérieur gauche) donnerait une aire négative.

## Ce que j'ai appris

- Prendre la valeur absolue du produit des différences est une façon simple de rendre le calcul d'aire indépendant de l'ordre des coins fournis.

## Améliorations possibles

Aucune : la solution est déjà O(1) et couvre correctement l'ordre arbitraire des coins.
