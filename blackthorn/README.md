# blackthorn

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `Blackthorn`)*

Thème : Chaînes de caractères

## Résumé

Déterminer si une chaîne donnée contient la sous-chaîne `"kth"`.

## Idée

Utiliser directement l'opérateur `in` pour tester la présence de la sous-chaîne.

Ça fonctionne parce que `in` sur des chaînes teste l'appartenance en tant que sous-chaîne (pas seulement caractère par caractère), ce qui correspond exactement à la question posée : pas besoin d'implémenter une recherche de motif à la main.

## Algorithme

1. Lire la chaîne `s`.
2. Tester si `"kth"` est une sous-chaîne de `s`.
3. Afficher `yes` ou `no` en conséquence.

## Complexité

- Temps : O(n), n étant la longueur de `s`.
- Mémoire : O(1) en plus de la chaîne d'entrée.

## Difficultés rencontrées

Aucune difficulté particulière : c'est un test d'appartenance direct, sans cas limite notable au-delà d'une chaîne plus courte que `"kth"` (auquel cas `in` renvoie simplement `False`, sans erreur).

## Ce que j'ai appris

- L'opérateur `in` sur les chaînes Python gère nativement la recherche de sous-chaîne, sans risque d'erreur même si la chaîne d'entrée est plus courte que le motif recherché.

## Améliorations possibles

Aucune : la solution est déjà la plus directe possible pour ce test.
