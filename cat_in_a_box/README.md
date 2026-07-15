# cat_in_a_box

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `CatInABox`)*

Thème : Implémentation

## Résumé

Comparer le volume d'un chat (approximé par une boîte h×w×l) au volume d'une boîte de capacité `c`, et indiquer si le chat a trop d'espace, juste ce qu'il faut, ou pas assez.

## Idée

Calculer le volume `h*w*l` et le comparer directement à `c` avec trois comparaisons indépendantes.

Ça fonctionne parce que le problème se réduit à comparer deux entiers ; aucune structure de données ni algorithme complexe n'est nécessaire.

## Algorithme

1. Lire `h`, `w`, `l`, `c`.
2. Calculer le volume `h*w*l`.
3. Afficher `SO MUCH SPACE`, `COZY` ou `TOO TIGHT` selon que le volume est supérieur, égal ou inférieur à `c`.

## Complexité

- Temps : O(1).
- Mémoire : O(1).

## Difficultés rencontrées

Le volume `h*w*l` est recalculé trois fois (une fois par `if`) au lieu d'être stocké dans une variable : ça ne change pas la correction du programme mais c'est redondant.

## Ce que j'ai appris

- Trois `if` indépendants (au lieu de `if/elif/else`) fonctionnent ici car les trois conditions sont mutuellement exclusives, mais un `if/elif/else` communique mieux cette exclusivité au lecteur.

## Améliorations possibles

```python
volume = h * w * l
if volume > c:
    print("SO MUCH SPACE")
elif volume == c:
    print("COZY")
else:
    print("TOO TIGHT")
```
