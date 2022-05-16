# 9 - Algorithmique du texte. Exemples et applications. #

## Version Olivier Carton ##

Bibliographie : cf. Moodle ( Maxime Crochemore )

Raisonnable de faire $\binom{4}{3}$, voire même $\binom{4}{2}$ parties, les quatre ça fait presque trop

1. Recherche de motifs
   * KMP (automate dans l'idée mais pas dans l'implémentation, faire attention [NdY sauf pour haddad]), BB, Hachage
   * Aho - Corasick
   * Automates (expressions rationnelles)
1. Indexation (HORS PROGRAMME / 20, je crois) [NDF : Quoi, on ne fait jamais de HP en cours voyons ! [NdA : sel]] [Nd∞ : En vrai la HP ça sert à la leçon, ça peut faire un dvt stylé]
   * Arbre des suffixes (structure de données). Algo de McCreight
   * Directed Acyclic Word Graph (DAWG)
   * Table des suffixes (linéaire, permet de faire à peu près comme arbre des suffixes)
1. Compression
   * Huffman
   * Lempel Ziv
   * Grammar Based Code
   * Transformation de Burrows-Wheeler (gzip)
1. Alignement de séquences
   * Plus longue sous-chaîne [NdA : mon correcteur me propose sous-chemise...]
   * Distance d'édition
   * Application à la biologie


## Version Aurore ##

### Source ###

???

### [Notes](notesAB.md) ###

### Plan ###

[Plan détaillé](planAB.pdf)

1. Notions importantes
2. Recherche de motif dans un texte
   1. Algorithme naïf
   2. Optimiser le déplacement
	  1. Sans automate: Boyer-Moore
	  2. Avec automate: Knuth-Morris-Pratt
	     * Dev 1 = etude algo
   3. Utilisation de la table de hachage
3. Mesures de similarité
   1. Distances
   2. Plus longue sous-séquence commune
	  * Dev 2 = algo + optim mémoire
4. Compression de texte
   1. Algorithme de Huffman
   2. Algorithme de Lempel-Zir-Welch

### Développements ###

- Dev 1 : étude de l'algorithme de Knuth-Morris-Pratt
- Dev 2 : Algorithme de la plus longue sous-séquence commune + optimisations mémoire
