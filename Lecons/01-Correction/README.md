# 1 - Exemples de méthodes et outils pour la correction des programmes. #

## Version Thomas ##

### Sources ###

- Plan : doc de SQLite: comment SQLite est testé

- Dev 1 : le règle des sémantiques à grand et petit pas de IMP.

- Dev 2 : MÜLLER-OLM, Markus, SCHMIDT, David, et STEFFEN, Bernhard. Model-checking. In : International Static Analysis Symposium. Springer, Berlin, Heidelberg, 1999. p. 330-354.

### [Notes](notesTM.md) ###

### Plan ###

[Plan détaillé](planTM.pdf)

1. Validation (preuve de correction)
   1. Typage
   2. Sémantique
	  1. Sémantique à grands pas
	  2. Sémantique à petits pas
	  3. Exemple de sémantique d'un langage
	     * Dev 1
   3. Outils mathématiques pour la preuve de correction
	  1. Ordre bien fondé
	  2. Variants et invariants
	  3. Structure de Kripke
	     * Dev 2
2. Verification (test de correction)
   1. White/Blackbox
   2. Tests aléatoires
   3. Tests adaptatifs
   4. Evaluation de la qualité des tests: couverture
	  1. Statement coverage
	  2. Branch coverage
	  3. Couverture des limites
	  4. Modified condition / decision coverage

### Développements ###

- Dev 1 : exemple de sémantique
- Dev 2 : présentation des structures de Kripke. [Notes](TM-kripke.pdf)

## Adjacent: "Preuve et correction de programme" par Axel ##

[Plan](adj/planAK.pdf)
[Notes](adj/notesAK.pdf)
