# 28 - Formules du calcul propositionnel : représentation, formes normales, satisfiabilité. Applications. #

## Version Emmanuel ##

### Sources ###

???

### [Notes](notesEB.md) ###

### Plan ###

[Plan détaillé](planEB.pdf)

1. Syntaxe et sémantique
   1. Syntaxe, "l'écriture des formules"
   2. Sémantique, "le sens des formules"
	  1. Modèle
	  2. Propriétés formules
	  3. Théorie
2. Substitutions et formes normales
   1. Substitutions
   2. Formes normales
	  1. Négative (NNF)
	  2. Conjonctive (CNF)
	     * Dev 1 = implémentation transformation Tseitin
	  3. Disjonctive (DNF)
	  4. Complete
	  5. Première
   3. Satisfiabilité
3. Théorie de la preuve
   1. Déduction naturelle
	  * Dev 2 = éléments de preuve du théorème de complétude
   2. Calcul des séquents
4. Ouverture

### Développements ###

- Dev 1 : implémentation de la transformation de Tseitin, en OCaml
- Dev 2 : éléments de preuve pour le théorème de la complétude propositionnelle
