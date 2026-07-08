# king_arthur_round_table

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `KingArthurRoundTable`)*

## Résumé

Déterminer si un nombre donné de chevaliers, chacun occupant une largeur fixe, peut s'asseoir autour d'une table ronde d'un diamètre donné.

## Idée

Calculer la circonférence de la table (`π × diamètre`) et la comparer à l'espace total requis (`largeur d'un chevalier × nombre de chevaliers`).

Ça fonctionne parce que les chevaliers sont assis côte à côte le long du bord circulaire de la table : l'espace disponible est exactement la circonférence, et l'espace nécessaire est la somme des largeurs. Pas besoin de géométrie plus poussée, c'est une simple comparaison de longueurs.

## Algorithme

1. Lire le diamètre, la largeur d'un chevalier et le nombre de chevaliers.
2. Calculer la circonférence avec `π × diamètre`.
3. Comparer l'espace requis à la circonférence et afficher `YES` ou `NO`.

## Complexité

- Temps : O(1).
- Mémoire : O(1).

## Difficultés rencontrées

Utiliser `<=` et non `<` : le cas où l'espace requis est exactement égal à la circonférence doit être accepté (`YES`).

## Ce que j'ai appris

- `math.pi` donne une précision suffisante pour ce genre de problème géométrique simple ; pas besoin de gérer soi-même une valeur approchée de π.

## Améliorations possibles

Aucune : la solution est déjà O(1) et directe.
