# getting_wood

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `gettingWood`)*

Thème : Chaînes de caractères

## Résumé

Chercher la première occurrence du mot `"tree"` dans une chaîne et afficher son indice, ou un message si le mot est absent.

## Idée

Tester d'abord la présence de `"tree"` avec `in`, puis utiliser `str.index()` pour récupérer sa position seulement si elle existe.

Ça fonctionne parce que `str.index()` lève une exception si la sous-chaîne est absente : la vérifier avec `in` avant d'appeler `index()` évite l'exception et permet d'afficher le message alternatif proprement.

## Algorithme

1. Lire la chaîne `s`.
2. Si `"tree"` n'apparaît pas dans `s`, afficher `no trees here`.
3. Sinon, afficher l'indice de la première occurrence avec `s.index("tree")`.

## Complexité

- Temps : O(n), n étant la longueur de `s` (la recherche de sous-chaîne est linéaire en pratique).
- Mémoire : O(1) en plus de la chaîne d'entrée.

## Difficultés rencontrées

Le test `in` et l'appel à `index()` recherchent tous les deux la sous-chaîne indépendamment : la chaîne est donc parcourue deux fois dans le pire cas. Ça reste négligeable ici mais serait à éviter sur une entrée très longue.

## Ce que j'ai appris

- `str.find()` renvoie `-1` au lieu de lever une exception quand la sous-chaîne est absente, ce qui permet de combiner recherche et vérification en un seul appel.

## Améliorations possibles

```python
s = input()
i = s.find("tree")
print("no trees here" if i == -1 else i)
```
Une seule recherche au lieu de deux.
