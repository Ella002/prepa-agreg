# 26 - Classes P et NP. Problèmes NP-complets. Exemples. #

## Version Jules ##

### Sources ###

Source principale : CLRS (Cormen)

Pour le DEV 1 :
- Pas de source particulière (je n'ai pas trouvé de livre qui contient cette preuve, seulement des articles scientifiques et Wikipédia)
  NB : J'ai appris le que livre du prof d'IA (les 126 algos qu'il faut avoir codé dans sa vie) contient un algo linéaire pour 2-SAT.

Pour le DEV 2 :
- Hopcroft, Motwani et Ullman, _Introduction to Automata Theory, Languages and Computation_, Third Edition, Pearson, 2014
  Pas la preuve complète, mais un exercice très guidé.

Pour le DEV 3 :
- Goodrich et Tamassia, _Algorithm Design and Applications_, Wiley, 2015
  Pour l'algorithme de couplage parfait de poids minimal : Lovász et Plummer, _Matching Theory_, North-Holland, 1986

### [Notes](notesJS.md) ###

### Plan ###

[Plan détaillé](planJS.pdf)

1. La classe P
   1. Problèmes de décision P
	  * Dev 1 = 2-SAT est P
   2. Généralisation aux problèmes d'optimisation
2. La classe NP
   1. Problèmes de décision NP
   2. Problèmes d'optimisation NP
3. Problèmes NP-complets et approximations
   1. Clique
	  * Dev 2 = clique-cover est NP-complet
   2. Couverture de sommets
   3. Cycle hamiltonien
	  * Dev 3 = TSP admet une 3/2-approximation en temps polynomial

### Développements ###

- Dev 1 = preuve que 2-SAT est P
- Dev 2 = preuve que CLIQUE-COVER est NP-complet
- Dev 3 = preuve que TSP admet une 3/2-approximation en temps polynomial
