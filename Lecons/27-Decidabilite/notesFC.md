# 12/01 - 27. Décidabilité et indécidabilité. Exemples. - Fanny #



Développements :

   * **Décidabilité de l'arithmétique de Presburger <- choisi par """l'assemblée"""**
   * Indécidabilité de PCP


## Développement ##



- def arithmétique de Presburger :

   * \forall et \exists, ou, et, neg
   * variables, 0, 1
   * + et =


Formule close (ie sans variable libre), sous forme prénexe (tous les quantificateurs en tête, on admet que c'est possible) : Q\_1 x\_1 Q\_2 x\_2 [...] Q\_n x\_n \psi où q\_i quantificateur, \phi sans quantificateurs



On va construire un automate qui va accepter exactement les suites de n-uplets de bits qui encodent les variables.

\phi\_k = Q\_{k+1} x\_{k+1} ... Q\_n x\_n \psi

(en particulier \phi\_0 = \phi et \phi\_n = \psi)



## Questions et remarques ##



GD : Pourquoi faire prénexe ?

   * C'est pas forcément utile ? MAIS les bouquin font comme ça


GD : Pourquoi mots little endian et pas big endian?

   * Ça faisait des choses bizarres sinon. Et c'est ce que font les bouquins.


GD : Que reconnaît l'automate construit pour phi\_k?

   * Entrée = k-uplet, reconnaît mot codant les k variables qui satisfont la formule (ie donne des valeurs aux variables libres de la formule)


GD : Comment on appelle une fonction qui donne des valeurs aux variables libres d'une formule? Est-ce qu'on peut associer une variable de vérité?

   * Valuation / Environnement / Assimilation (Borgs?)
Ici on reconnaît les valuations



GD : Comment on code un k-uplet dans l'alphabet {0,1}^k?

   *  on fait des colonnes, première ligne = valuation de x1, 2ème de x2...


SG: Si on fait la même chose dans les réels plutôt que les entiers, c'est décidable ?

   * problème de codage: pas forcèment d'écriture finie
Réponse de SG: c'est plus gros mais c'est plus facile



Question d'Hugo : Comment gérer les autres cas de l'initialisation (x = 0 ou x + y = z + w)



GD : Si t'as x + y + z = w?

   * On peut le transformer en E u, x + y = u et z + u = w, et on se ramène au cas ci-dessus
GD : Pour x = 0 et x = 1 ?

   * (réponse)


SG : Y a-t-il plus de problèmes décidables ou indécidables ?

   * Nombre indénombrable de langages, nombre dénombrable de MT


SG : C'est quoi une grammaire ambiguë ?

   * Un grammaire qui contient un mot qui peut être atteint par plusieurs réductions différents
SG : attention à la déf de "réduction". C'est sur les arbres de dérivation, pas la suite des opérations (qui peut confluer vers le même arbre)



C'est pas mal du tout ! Vraiment équilibré, complet! (NDLR : Ui)



GD : vous avez dit "c'est bien de savoir que c'est indécidable, ça évite de chercher indéfiniment un algorithme quand il n'y en a pas". Vous avez un exemple ?

Rep (GD) : Le 10ème problème de Hilbert



## Remarques ##



### Sur le développement ###



   * Manque de vocabulaire sur la partie logique
   * "Construire la machine de Turing" : soit tu la construis entièrement (pas ça le jour de l'agreg), soit tu donnes juste l'algorithme sans dire que tu donnes la machine de Turing
   * Peut-être inclure les raisons pour lesquelles ça marche pas avec la multiplication
   * Les + : Temps maîtrisé, bon degré de détails! Finir sur des exemples.




### Sur le plan ###



   * Très bien : montrer le recul sur la calculabilité (MT mais aussi λ-calcul, fonctions récursives)
   * Pas utiliser le terme "naturel" en parlant de la thèse de Church, parler plutôt d'absolu (laissons les oiseaux tranquilles)
   * Y a problèmes décidables, et aussi notion d'ensembles d'entier décidable (hein?)
   * Pas de mention de la machine universelle, plutôt utiliser ce vocabulaire que "langage L-appartient"
   * Le moment de l'argument diagonal, c'est l'occasion de détendre l'atmosphère avec un point historique
   * Insister sur la paradoxe : pour montrer qu'un problème est indécidable, parfois il "suffit" de programmer : le principe de réduction, c'est de donner une fonction ***calculable*** qui la transforme en un problème connu indécidable
   * Historiquement, on savait trouver des algos pour les problèmes décidables bieeeeeen avant d'être capable de déterminer qu'un problème est indécidable
   * Pas de mention des machines RAM
   * Mention de grammaire ambigüe: qu'est-ce? Etant donné une grammaire hors contexte, elle est ambigüe s'il existe des mots du langage pour lesquels il y a plusieurs arbres de dérivations différents


Conclusion: très les compliments. Dowek il dit que c'est une leçon qui fait avoir l'agreg!



Sur les réels, c'est décidable, mais pas comme ça, ça s'appelle le théorème de Tarski, qui fonctionne en éliminant les quantificateurs (exemple : changer "\exists X, aX²+bX+c =0" en "b²-4ac >= 0")
