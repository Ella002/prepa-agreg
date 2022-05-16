# 5 - Implémentations et applications des piles et des files. #

## Version Fanny ##

### Source ###

- [Types de données et algorithmes, Froidevaux, Gaudel, Soria](https://www.lri.fr/~chris/LivreAlgorithmique/FroidevauxGaudelSoria.pdf)
- ???

### [Notes](notesFC.md) et [rapport](rapportFC.txt) ###

### Plan ###

[Plan détaillé](planFC.pdf)

1. Les piles
   1. Définition
   2. Exemples d'implémentation
	  1. Représentation contiguë
	  2. Représentation chaînée
	  3. Comparaison des deux méthodes
   3. Applications
	  * Dev 1 = implem du balayage de Graham
2. Les files
   1. Définition
   2. Exemples d'implémentation
	  1. Représentation contiguë
	  2. Représentation chaînée
	  3. Comparaison des représentations
   3. Applications
3. Lien entre pile et file et extensions
   1. Représentation des piles en files et vice-versa
   2. Structures dérivées
	  1. Files à double entrée
	  2. Files de priorité
	     * Dev 2 = implem avec tas binomial

### Développements ###

- Développement 1 : implémentation du balayage de Graham
  [Code](FC-dev1_graham.py)

- Développement 2 : implémentation de file de priorité
  [Code](FC-dev2_tas_binomial.ml)
