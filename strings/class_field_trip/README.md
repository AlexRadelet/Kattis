# class_field_trip

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `ClassFieldTrip`)*

## Résumé

Étant donné deux chaînes, concaténer leurs caractères et afficher le résultat trié.

## Idée

Concaténer les deux chaînes puis trier l'ensemble des caractères avec `sorted()`, avant de les rejoindre en une seule chaîne avec `"".join(...)`.

Ça fonctionne parce que `sorted()` appliqué à une chaîne la traite comme une séquence de caractères et renvoie une liste triée ; il ne reste plus qu'à la reconvertir en chaîne. C'est la façon la plus directe de "fusionner et trier" des caractères en Python, sans tri manuel.

## Algorithme

1. Lire les deux chaînes `ann` et `ben`.
2. Les concaténer en une seule chaîne `s`.
3. Trier les caractères de `s`.
4. Rejoindre les caractères triés et afficher le résultat.

## Complexité

- Temps : O(n log n), n étant la longueur totale des deux chaînes (coût du tri).
- Mémoire : O(n) pour la chaîne concaténée et la liste triée.

## Difficultés rencontrées

`sorted()` trie selon l'ordre des points de code Unicode : les majuscules sont donc triées avant les minuscules. À vérifier si l'énoncé attend un tri insensible à la casse.

## Ce que j'ai appris

- `sorted(chaîne)` renvoie une liste de caractères, pas une chaîne : il faut toujours repasser par `"".join(...)` pour reconstituer une chaîne.

## Améliorations possibles

Aucune pour ce problème simple ; si un tri insensible à la casse était requis, on utiliserait `sorted(s, key=str.lower)`.
