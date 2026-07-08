# gnome_sequencing

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `gnomeSequencing`)*

## Résumé

Pour plusieurs lignes de tailles de gnomes, déterminer si chaque ligne est ordonnée (croissante ou décroissante) ou non.

## Idée

Comparer chaque ligne à sa version triée en ordre croissant et à sa version triée en ordre décroissant : si elle correspond à l'une des deux, elle est ordonnée.

Ça fonctionne parce qu'une séquence est croissante si et seulement si elle est égale à sa propre version triée, et décroissante si et seulement si elle est égale à sa version triée à l'envers. Comparer aux deux versions triées est plus simple et moins sujet aux erreurs qu'un parcours manuel avec suivi de direction.

## Algorithme

1. Lire le nombre de lignes `n` et afficher l'en-tête `Gnomes:`.
2. Pour chaque ligne, lire la séquence de tailles.
3. Comparer la séquence à `sorted(line)` et à `sorted(line, reverse=True)`.
4. Afficher `Ordered` si l'une des deux correspond, sinon `Unordered`.

## Complexité

- Temps : O(m log m) par ligne, m étant la taille de la ligne (deux tris par ligne).
- Mémoire : O(m) par ligne pour les versions triées.

## Difficultés rencontrées

Trier deux fois par ligne (`sorted(line)` et `sorted(line, reverse=True)`) est redondant : un seul parcours linéaire suffirait à détecter si une séquence est croissante, décroissante, ou ni l'un ni l'autre.

## Ce que j'ai appris

- Comparer à une version triée est une façon simple (mais pas optimale) de tester si une séquence est déjà ordonnée ; un parcours direct est en O(m) au lieu de O(m log m).

## Améliorations possibles

```python
increasing = all(line[i] <= line[i+1] for i in range(len(line)-1))
decreasing = all(line[i] >= line[i+1] for i in range(len(line)-1))
print("Ordered" if increasing or decreasing else "Unordered")
```
Passe de O(m log m) à O(m) par ligne, sans allouer de listes triées supplémentaires.
