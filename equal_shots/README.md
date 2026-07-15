# equal_shots

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `EqualShots`)*

Thème : Implémentation

## Résumé

Deux groupes de boissons sont décrits chacun par une liste de paires (volume, concentration en alcool). Déterminer si la quantité totale d'alcool pur est la même dans les deux groupes.

## Idée

Pour chaque groupe, accumuler la somme des produits `volume × concentration` (la quantité d'alcool pur de chaque boisson), puis comparer les deux totaux.

Ça fonctionne parce que la quantité d'alcool pur d'une boisson est proportionnelle au produit de son volume par sa concentration ; sommer ces produits donne la quantité totale d'alcool du groupe, indépendamment du nombre ou de la répartition des boissons individuelles.

## Algorithme

1. Lire le nombre de boissons de chaque groupe (`a`, `b`).
2. Pour le groupe A, accumuler `v*c` pour chaque boisson lue.
3. Faire de même pour le groupe B.
4. Comparer les deux totaux et afficher `same` ou `different`.

## Complexité

- Temps : O(a + b).
- Mémoire : O(1).

## Difficultés rencontrées

Les totaux sont des entiers (`map(int, ...)`) : la comparaison `!=` est donc exacte, sans souci d'imprécision flottante. Si les valeurs d'entrée pouvaient être décimales, il faudrait comparer avec une tolérance plutôt qu'une égalité stricte.

## Ce que j'ai appris

- Accumuler pendant la lecture (sans stocker les listes) suffit dès qu'on n'a besoin que d'un total, ce qui économise de la mémoire.

## Améliorations possibles

Aucune : la solution est déjà linéaire et n'utilise que la mémoire strictement nécessaire.
