# penultimate

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `PenultimateIceCream`)*

Thème : Tri

## Résumé

Étant donné une liste de prix, afficher le deuxième prix le plus élevé (l'avant-dernier une fois trié).

## Idée

Trier la liste des prix par ordre croissant et prendre l'avant-dernier élément (`sorted_prices[-2]`).

Ça fonctionne parce que trier place naturellement le plus grand élément en dernière position et le deuxième plus grand juste avant. Trier est un peu plus coûteux qu'une recherche linéaire du top-2, mais reste largement suffisant vu les contraintes typiques de ce genre de problème, et le code est trivial à relire.

## Algorithme

1. Lire `n` (non utilisé directement mais fait partie du format d'entrée).
2. Lire la liste des prix.
3. Trier la liste.
4. Afficher l'avant-dernier élément.

## Complexité

- Temps : O(n log n) à cause du tri.
- Mémoire : O(n) pour la liste triée.

## Difficultés rencontrées

Si la liste contient des doublons au sommet (ex: deux fois le prix maximum), `sorted_prices[-2]` renvoie quand même la bonne valeur au sens de l'énoncé (le deuxième prix dans l'ordre trié, pas nécessairement un prix strictement inférieur). Il faut être sûr que c'est bien ce que demande le problème.

## Ce que j'ai appris

- Pour un simple "top-2", trier est plus lisible qu'un suivi manuel de max/second max, même si ce n'est pas optimal en complexité.

## Améliorations possibles

Un passage unique en O(n) permettrait de suivre `max1` et `max2` sans trier toute la liste, utile si `n` devient très grand :
```python
max1, max2 = float("-inf"), float("-inf")
for p in prices:
    if p > max1:
        max1, max2 = p, max1
    elif p > max2:
        max2 = p
```
