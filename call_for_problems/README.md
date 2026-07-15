# call_for_problems

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `CallForProblem`)*

Thème : Implémentation

## Résumé

Compter combien de numéros de problèmes, parmi une liste lue en entrée, sont impairs.

## Idée

Parcourir chaque numéro lu et incrémenter un compteur lorsque le reste de la division par 2 est non nul.

Ça fonctionne parce que la parité d'un entier se teste directement avec l'opérateur modulo : `problem % 2 != 0` est vrai exactement pour les nombres impairs. Compter en une seule passe évite de stocker la liste complète.

## Algorithme

1. Lire le nombre de problèmes `n`.
2. Pour chaque problème, lire son numéro.
3. Incrémenter `SUM` si le numéro est impair.
4. Afficher `SUM`.

## Complexité

- Temps : O(n).
- Mémoire : O(1).

## Difficultés rencontrées

Aucune difficulté particulière : le test de parité par modulo est le cas standard.

## Ce que j'ai appris

- `x % 2 != 0` est équivalent à `x % 2 == 1` pour des entiers positifs, mais reste correct aussi pour des entiers négatifs en Python (contrairement à d'autres langages où `%` peut renvoyer un reste négatif).

## Améliorations possibles

```python
n = int(input())
print(sum(1 for _ in range(n) if int(input()) % 2 != 0))
```
Équivalent, en une seule expression.
