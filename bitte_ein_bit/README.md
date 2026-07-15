# bitte_ein_bit

Lien vers Kattis : *(à compléter — nom de la fonction d'origine : `BitteeinBit`)*

Thème : Implémentation

## Résumé

Afficher le premier caractère de la chaîne lue en entrée.

## Idée

Lire la chaîne et en extraire directement le premier caractère avec l'indexation `[0]`.

Ça fonctionne parce que l'indexation de chaînes en Python donne un accès direct O(1) à n'importe quelle position, donc pas besoin de boucle pour récupérer uniquement le premier caractère.

## Algorithme

1. Lire la chaîne d'entrée.
2. Afficher son caractère à l'indice 0.

## Complexité

- Temps : O(1) (en ignorant le coût de la lecture de la ligne).
- Mémoire : O(1).

## Difficultés rencontrées

Si la chaîne d'entrée peut être vide, `input()[0]` lève une `IndexError`. À vérifier si l'énoncé garantit une chaîne non vide.

## Ce que j'ai appris

- Pas de notion particulière ici au-delà de l'indexation directe des chaînes ; c'est le genre de problème "un-liner" typique des exercices d'échauffement Kattis.

## Améliorations possibles

Aucune, sauf gestion explicite d'une entrée vide si nécessaire.
