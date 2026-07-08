# betting

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `betting`)*

## Résumé

Étant donné une probabilité de victoire exprimée en pourcentage, afficher les cotes "juste" (fair odds) pour parier sur la victoire et sur la défaite.

## Idée

Convertir le pourcentage en probabilité (`x/100`), puis calculer la cote comme l'inverse de la probabilité : `1/x` pour la victoire, `1/(1-x)` pour la défaite (probabilité complémentaire).

Ça fonctionne parce que dans un pari "juste", la cote décimale est l'inverse de la probabilité de l'évènement : plus un évènement est probable, plus sa cote est faible. La probabilité de défaite est le complément de celle de victoire (`1 - x`), donc calculer `1/(1-x)` donne directement sa cote.

## Algorithme

1. Lire le pourcentage `x` et le convertir en probabilité.
2. Afficher `1/x` (cote de victoire) avec 8 décimales.
3. Afficher `1/(1-x)` (cote de défaite) avec 8 décimales.

## Complexité

- Temps : O(1).
- Mémoire : O(1).

## Difficultés rencontrées

Si `x` vaut 0 ou 100, l'une des deux divisions (`1/x` ou `1/(1-x)`) provoque une division par zéro. Il faut vérifier si l'énoncé garantit `0 < x < 100`.

## Ce que j'ai appris

- La cote "juste" d'un pari est simplement l'inverse de la probabilité ; c'est une relation directe qui ne nécessite aucune structure de données.

## Améliorations possibles

Aucune, sauf gestion explicite des cas limites `x = 0` ou `x = 100` si l'énoncé ne les exclut pas.
