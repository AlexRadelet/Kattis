# shandy

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `Shandy`)*

## Résumé

Étant donné une quantité de bière (`B`) et de limonade (`L`), calculer le volume maximal de shandy (mélange à parts égales) réalisable.

## Idée

Le facteur limitant est l'ingrédient le moins abondant : on peut préparer `min(B, L)` unités de chaque ingrédient à parts égales, donc `min(B, L) * 2` unités de mélange au total.

Ça fonctionne parce qu'un shandy nécessite une quantité égale de bière et de limonade ; dès que l'un des deux ingrédients est épuisé, on ne peut plus augmenter le mélange. C'est un raisonnement classique de "goulot d'étranglement" (bottleneck), similaire à la limitation par la ressource la plus rare.

## Algorithme

1. Lire la quantité de bière `B`.
2. Lire la quantité de limonade `L`.
3. Afficher `min(B, L) * 2`.

## Complexité

- Temps : O(1).
- Mémoire : O(1).

## Difficultés rencontrées

Aucune difficulté particulière : le piège serait d'oublier le facteur 2 (le mélange contient deux fois `min(B, L)`, pas seulement la quantité de l'ingrédient limitant).

## Ce que j'ai appris

- Beaucoup de problèmes "ressources limitées" se résument à un simple `min()` : identifier la ressource la plus contraignante règle le problème.

## Améliorations possibles

Aucune : la solution est déjà optimale et O(1).
