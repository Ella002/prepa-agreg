# 15 - Hiérarchie mémoire. Structure et performances. #

## Version Thomas ##

### Sources ###

???

### [Notes](notesTM.md) ###

### Plan ###

[Plan détaillé](planTM.pdf)

1. Structure du cache
   1. Structure en bloc
   2. Structure en oignon
   3. Transparence
   4. Métadonnées
   5. Performance
2. Choix d'implémentation
   1. Associativité
   2. Types d'adresses
   3. Politique d'écriture et d'allocation
	  1. Ecriture
	  2. Allocation
   4. Multicœur
	  1. Localité du cache
	  2. Cohérence
	     * Dev 1 = protocole MESI
3. Problématiques liées
   1. Optimisation
	  1. Séparer le cache donnée / cache instruction
	  2. Préchargement
	  3. Victim cache
	  4. Optimiser le code pour le cache
   2. Sécurité
	  * Dev 2 = attaque Spectre
   3. Autres formes de cache
	  1. TLB
	  2. SSD cache
	  3. SQL buffer cache

### Développements ###

- Dev 1 : protocole MESI
- Dev 2 : attaque Spectre
