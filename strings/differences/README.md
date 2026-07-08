# differences

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `differences`)*

## Résumé

Pour plusieurs paires de lignes de même longueur, afficher les deux lignes suivies d'une ligne de marqueurs indiquant à quelles positions les caractères diffèrent.

## Idée

Comparer les deux lignes caractère par caractère (via leurs indices) et construire une troisième chaîne où chaque position vaut `*` si les caractères diffèrent, `.` sinon.

Cette approche fonctionne parce que le problème garantit que les deux lignes d'une même paire ont la même longueur : on peut donc itérer sur les indices de `line1` sans risque de dépassement.

Une comparaison position par position est le choix naturel ici : il n'y a pas de structure à exploiter (pas de tri, pas de recherche), juste une correspondance terme à terme.

## Algorithme

1. Lire le nombre de paires `n`.
2. Pour chaque paire : lire `line1` et `line2`.
3. Construire `diff` en comparant `line1[j]` et `line2[j]` pour chaque indice `j`.
4. Afficher `line1`, `line2`, puis `diff` suivi d'une ligne vide.

## Complexité

- Temps : O(L) par paire, où L est la longueur des lignes (O(n·L) au total).
- Mémoire : O(L) pour stocker `diff`.

## Difficultés rencontrées

Le code suppose que `line1` et `line2` ont exactement la même longueur (`range(len(line1))`). Si ce n'est pas garanti par l'énoncé, il faudrait itérer sur `min(len(line1), len(line2))` pour éviter un `IndexError`.

## Ce que j'ai appris

- Construire une chaîne caractère par caractère avec `+=` fonctionne mais une compréhension avec `zip(line1, line2)` serait plus idiomatique et évite de dépendre des indices.

## Améliorations possibles

Remplacer la boucle indexée par :
```python
diff = "".join("*" if a != b else "." for a, b in zip(line1, line2))
```
Plus lisible et plus sûr si les longueurs peuvent différer légèrement (s'arrête à la plus courte au lieu de planter).
