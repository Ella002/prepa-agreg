# 09/02 - 09. Algorithmique du texte. Exemples et applications. — Aurore #



Développements :

   * Étude de l'algorithme de Knuth-Morris-Pratt
   * **Algorithme de la plus longue sous-séquence commune + Optimisation mémoire <- choisi par le jury**


## Questions ##

### Sur le développement ###


Q (SS) : Dans le calcul de longueur, il y a une confusion entre les n et les m, n n’apparaît pas dans l'algo alors que c'est la longueur du tableau

R : Effectivement, c'est une confusion



Q (SS) : Sur l'explication informelle, que se passe-t-il si n est impair ?

R : (Typo au tableau sur les parties entières de divisions par 2)



Q (SS) : comment est-ce que vous arrivez à la complexité en temps que vous donnez ? (Note : durant la présentation, l'argument donné était : par récurrence, sans expliciter la récurrence)

R : (développé au tableau en dessous du résultat) Propriété prouvée par récurrence : $$P(m) = \forall i \leq m, T(i m) \leq 2 C i m$$



Q (SS) : Qu'est-ce qui fait qu'on peut utiliser de la programmation dynamique en général ?

R : Quand on peut établir une récurrence selon les résultats de sous-problèmes (SS) La solution optimale peut être exprimée à partir de solutions sur les sous-problèmes.



Q (OC) : Visuellement qu'est-ce que ça représente la recherche du $k$ ?

R : *Explication avec un dessin, trouver le point d'intersection qui minimise la longueur du chemin total*



Q (SS) : Est-ce qu'il y a une autre façon d'optimiser "un peu tout" dans un algo de prog dyn ?

R : Diviser pour régner

Q (SS) : Par exemple, est-ce que ça vaut le coup de calculer toutes les entrées dans votre matrice ?

R (SS) : Mémoïsation



### Sur le plan ###



Q (OC) : si on veut chercher plusieurs mots dans une recherche de motifs, qu'est-ce qu'on fait ?

R : Prétraitement des motifs entre eux.

Q (OC) : Comment adapter KMP pour plusieurs mots ?

R : Pour l'automate de KMP, on peut faire un automate (pas en ligne) qui prend en compte tous les mots.

Q (OC) : Et à la fin, on a construit quoi ? [NdA : automate de Sigma*(mot1|mot2|mot3...), mais du coup c'est pas un arbre non ?]

R : Un graphe en quelque sorte...

Q (OC) : Exemple : on veut matcher "aba", "aab" et "baa". À quoi correspondent les nœuds de l'arbre associé ?

R : Ils correspondent aux préfixes de chacun des mots



Q (SS) : Quelle est la notion illustrée par le calcul de cet automate ?

R : C'est des bordures



Q (SS) : Est-ce que vous avez des garanties sur la taille de l'automate ?

R : Nombre de motifs = $k$, motifs de taille $m\_i$ => au plus $\sum m\_i$ états

Q (SS) : Quid du nombre de transitions ?

R : Il faudrait prendre en compte la taille de l'alphabet.

Q (SS) : C'est le sens [NdA : je trouvais ça vachement mieux avec l'essence !] de ma question. Y en a-t-il besoin ? [NdA : on accepte des transitions par défaut comme 1 seule transition]

R (SS) : En autorisant les transitions par défaut remontant à la racine, les autres transitions sont aussi en $O(\sum m\_i)$.



Q (SS) : Si on veut la plus longue sous-séquence commune à 3 mots par exemple, comment on fait ?

R : Je dirais qu'on regarde la plus longue entre $u\_1$ et $u\_2$, puis la plus longue sous-séquence commune entre ça et $u\_3$ [NdA : ca marche pas je crois, fab, abf, f. Please prove me wrong]

Q(SS) : plus longue sous-séquence commune de $N$ mots, ça a une bonne complexité ?

R : Ca va être en $O(\log(N))$ ? Après réflexion, sur un exemple, plutôt on $O(N*C(n))$ ou $C(n)$ est la complexité de le recherche de sous-séquence sur des mots de longueur $n$



Q(OC) : Vous avez parlé d'Huffman : on lit, on calcule les séquences, on calcule le code. C'est comme ça qu'on fait en pratique ou pas ? #CestCulturel

R (OC) : En pratique, on adapte l'arbre au fur et à mesure qu'on lit le mot, pour ne pas lire plusieurs fois le mot. Si le fichier est pas trop tordu, on converge vite vers les bonnes fréquences





## Remarques ##



Huffman adaptatif

LZW : Construction des grammaires algébrique "straight-line programmed"



### Sur le développement ###



OC : Expliquer l'algo avec un dessin !

OC : Quand on fait les trucs que avec les mains, on est sûr de pas se planter dans les indices



### Générales ###



Attention à pas trop être sur les notes.



Il faut illustrer tous ces algos sur des dessins dans le développement de cette leçon, car ils sont très abstraits. [NDF probablement applicable sur toutes les leçons]

[NdY : c'était cool dans le plan parce qu'il y a plein de dessins]

+ Faire des exemples à toutes les étapes dans le dvpt, permet de gagner du temps sur des explications ailleurs donc ça fait pas plus long en tout



Attention : recherche de motif naïve linéaire dans le meilleur des cas (échec à la 1ere lettre tout le temps)



Mentionner les applications en bio-info, recherche de motifs ADN



## Proposition de plan par OC ##

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
