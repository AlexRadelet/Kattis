# fallen_chimney

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `FallenChimney`)*

Thème : Implémentation

## Résumé

Parmi une série de mesures accompagnées d'un verdict "nej" (non sécurisé) ou autre, trouver la plus grande valeur associée au verdict "nej".

## Idée

Parcourir chaque ligne, et à chaque fois que le verdict vaut `"nej"`, mettre à jour un maximum courant `secure` si la valeur lue est plus grande.

Ça fonctionne parce que le problème ne demande le maximum que parmi un sous-ensemble filtré des mesures (celles marquées `"nej"`) : combiner filtrage et suivi du maximum en une seule passe évite de stocker toutes les mesures pour les filtrer ensuite.

## Algorithme

1. Lire `n`.
2. Pour chaque ligne, lire la mesure et son verdict.
3. Si le verdict est `"nej"` et que la mesure dépasse `secure`, mettre à jour `secure`.
4. Afficher `secure`.

## Complexité

- Temps : O(n).
- Mémoire : O(1).

## Difficultés rencontrées

La variable de boucle `i` est réutilisée pour stocker la mesure lue (`i, note = input().split()`), ce qui écrase la variable d'itération du `for i in range(n)`. Le code reste correct ici car `i` n'est pas réutilisé comme compteur après cette ligne, mais c'est une source de confusion à la lecture et un bug potentiel si la boucle dépendait de sa valeur.

## Ce que j'ai appris

- Réutiliser un nom de variable de boucle pour autre chose dans le corps de la boucle fonctionne en Python mais nuit à la lisibilité et peut cacher des bugs si le nom est réutilisé ailleurs.

## Améliorations possibles

Renommer la variable de boucle pour éviter le conflit :
```python
n = int(input())
secure = 0
for _ in range(n):
    value, note = input().split()
    if note == "nej" and int(value) > secure:
        secure = int(value)
print(secure)
```
