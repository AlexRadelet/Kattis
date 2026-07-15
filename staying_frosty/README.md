# staying_frosty

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `StayingFrosty`)*

Thème : Implémentation

## Résumé

Déterminer si un poids `w` peut être supporté par `p` unités ayant chacune une capacité de 360, en comparant `w` à la capacité totale.

## Idée

Comparer directement `w` à `360 * p` (la capacité totale disponible) et répondre `YES` si elle est suffisante.

Ça fonctionne parce que la capacité totale est simplement la somme des capacités individuelles (360 par unité) : c'est une comparaison arithmétique directe, sans logique supplémentaire.

## Algorithme

1. Lire `w` et `p`.
2. Comparer `w` à `360 * p`.
3. Afficher `YES` si `w <= 360*p`, sinon `NO`.

## Complexité

- Temps : O(1).
- Mémoire : O(1).

## Difficultés rencontrées

La constante `360` n'est pas nommée : sans connaître l'énoncé exact, sa signification (capacité par unité ?) n'est pas évidente à la lecture du code seul.

## Ce que j'ai appris

- Nommer les constantes magiques (ex: `CAPACITY_PER_UNIT = 360`) rend le code auto-documenté, surtout utile pour un problème relu des mois plus tard.

## Améliorations possibles

```python
CAPACITY_PER_UNIT = 360
w, p = map(int, input().split())
print("YES" if w <= CAPACITY_PER_UNIT * p else "NO")
```
