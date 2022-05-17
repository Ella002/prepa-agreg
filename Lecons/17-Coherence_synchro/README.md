# 17 - Problèmes et stratégies de cohérence et de synchronisation. #

## Version Jules ##

### Sources ###

???

### [Notes](notesJS.md) ###

### Plan ###

[Plan détaillé](planJS.pdf)

Préliminaires
1. Section critique, exclusion mutuelle
   1. Exclusion mutuelle avec primitive forte
   2. Avec primitives read et write
	  * Dev 1 = boulangerie Lamport
2. Hiérarchie des primitives de synchronisation
   * Dev 2

### Développements ###

- Dev 1 : présentation de l'algorithme de la boulangerie de Lamport et preuve des propriétés
- Dev 2 : preuve du théorème
  "Tout registre dont les primitives sont RMW dans common2 et dont l'ensemble F n'est pas réduit à Id a un numéro de consensus de 2"
