# 11 - Exemples d’algorithmes d’approximation et d’algorithmes probabilistes. #

## Version Axel ##

### Sources ###

- Plan: Informatique MP2I et MPI, Vincent Barra. Chap 7, p 155-173

- Dev 1 : Approximation Algorithms, Vazirani et al. Pages 121-122
  Preuve plus complexe que celle présentée parce qu'on a pas besoin des solutions demi-entières dans la relaxation pour avoir l'approximation.
  Une 2-approximation est aussi disponible dans le Cormen, mais n'utilise pas de relaxation linéaire.

- Dev 2 : Chaum, David; Evertse, Jan-Hendrik; van de Graaf, Jeroen (1987). An Improved Protocol for Demonstrating Possession of Discrete Logarithms and Some Generalizations. Advances in Cryptology – EuroCrypt '87: Proceedings. Lecture Notes in Computer Science. Vol. 304. pp. 127–135. ISBN 978-3-540-19102-5 [Citation issue de wikipedia, pdf du contenu disponible à https://static.aminer.org/pdf/PDF/000/192/812/an_improved_protocol_for_demonstrating_possession_of_discrete_logarithms_and.pdf]
  Notes : preuve peu élaborée dans le bouquin : la correction est faite très rapidement et la coté zero-knowledge utilise un formalisme assez lourd repris (et mal expliqué) d'un autre papier.
  Le protocole est par contre bien représenté par un schéma. La page wikipedia des preuves zero-knowledge [https://en.wikipedia.org/wiki/Zero-knowledge_proof#Discrete_log_of_a_given_value] donne une version plus élaborée de la preuve de correction, mais toujours pas de preuve en profondeur du concept de simulateur utilisé pour définir et prouver le côté zero-knowledge.

### [Notes](notesAK.md) ###

### Plan ###

[Plan détaillé](planAK.pdf)

1. Algorithmes d'approximation
   1. Définitions
   2. 2-approximation du problème d'ordonnancement
   3. 2-approximation du problème du sac à dos
   4. 2-approximation de vertex cover par relaxation linéaire
	  * Dev 1
2. Algorithmes probabilistes
   1. Algorithmes de Las Vegas
   2. Algorithmes de Monte Carlo
	  * Dev 2 = preuve zero knowledge d'identité
3. Conclusion et ouvertures
   1. Algorithmes d'approximation
   2. Algorithmes probabilistes

### Développements ###

- Dev 1 : 2-approximation de vertex cover
  [Notes](AK-vertex_cover.pdf)

- Dev 2 : preuve zero-knowledge d'identité
  [Notes](AK-preuve_identite.pdf)
