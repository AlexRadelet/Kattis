# going_nuts

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `goingNuts`)*

## Résumé

Étant donné un entier, afficher le nombre de bits à 1 dans sa représentation binaire.

## Idée

Convertir l'entier en chaîne binaire avec le format `{:b}`, puis compter les caractères `'1'`.

Ça fonctionne parce que le format `b` de Python produit exactement la représentation binaire standard (sans préfixe `0b`), ce qui rend le comptage direct sans avoir à implémenter soi-même une conversion décimal → binaire.

## Algorithme

1. Lire l'entier.
2. Le formater en binaire avec `f"{n:b}"`.
3. Compter les caractères égaux à `'1'`.
4. Afficher le résultat.

## Complexité

- Temps : O(log n), la longueur de la représentation binaire.
- Mémoire : O(log n) pour la chaîne binaire.

## Difficultés rencontrées

Aucune difficulté majeure : le formatage intégré de Python évite les pièges classiques de conversion manuelle (division/modulo répétés, gestion du cas `n = 0`).

## Ce que j'ai appris

- `f"{n:b}"` est plus simple et moins sujet aux erreurs qu'une conversion manuelle en binaire.
- `bin(n).count('1')` fait la même chose de façon encore plus directe (`bin(n)` inclut un préfixe `0b`, mais celui-ci ne contient pas de `'1'` donc `count` reste correct).

## Améliorations possibles

```python
print(bin(int(input())).count("1"))
```
Équivalent, légèrement plus court.
