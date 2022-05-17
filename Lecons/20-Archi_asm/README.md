# 20 - Principes de fonctionnement des ordinateurs : architecture, notions d’assembleur. #

## Version Yaëlle ##

### Sources ###

- [Computer Organization and Design, Patterson and Hennessy](http://home.ustc.edu.cn/~louwenqi/reference_books_tools/Computer%20Organization%20and%20Design%20RISC-V%20edition.pdf). Chapitres 2 (asm) et 4 (archi processeur)

### [Notes](notesYV.md) ###

### Plan ###

[Plan détaillé](planYV.pdf)

1. Vue d'ensemble
2. Rendre la machine programmable: le langage assembleur
   1. Opérandes possibles
   2. Opérations arithmétiques et logiques
   3. Transfert de données
   4. Branchement conditionnel
   5. Fonctions
   6. Représentation binaire
	  * Dev 1 = reverse-engineering de code assembleur
3. Architecture du processeur: chemin de données
   * Dev 2 = construction chemin de données
   1. Parallélisme d'instructions: pipeline

### Développements ###

- Dev 1 : reverse-engineering de code risc-v
  [Code](YV-riscv.txt)
- Dev 2 : construction du chemin de données d'un processeur à partir d'un sous-ensemble d'instructions risc-v
