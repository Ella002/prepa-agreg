# 13/06 - 12.Stratégies algorithmiques (dont glouton, diviser pour régner, programmation dynamique, retour sur trace).-Jules

## Plan:
    algo par decompositions

        glouton, diviser pour regner, prog dyn

   algo par explo:
       backtracking
       separation et exploration
Conclusion

### developements:
    prog dyn sac-a-dos
    alpha-beta pour minimax <- choisi par le jury


## Développement : 
contexte : 
Pour des jeux
- à deux joueurs (Ah-damn et Eve)
- à information complète
- à somme nulle

Ensemble d'états finaux F, fonction d'évaluation h : F -> Z
Ève veut maximiser h, Adam veut minimiser h

Adam parce que \forall, Ève parce que \exists
[présente un exemple, sur un "jeu jouet"]

Fonction MiniMax(a):
    Si a feuille:
        renvoyer h(a)
    Si a noeud de Ève:
        renvoyer max_{e \in enfant de a} MiniMax(e)
    Sinon
        renvoyer min_{e \in enfant de a} MiniMax(e)

[explique que le calcul n'est pas nécessaire sur certaines branches]

Spec AlphaBeta(a, A, B)

Fonction AlphaBeta(a, A, B):
    Si a feuille:
        renvoyer h(a)
    Sinon:
        alpha = -\inf
        beta = +\inf
        Si a noeud de Ève:
            pour chaque enfant e de a:
                v = AlphaBeta(e, min(A, alpha), B)
                alpha = max(alpha, v)
    [se fait interrompre : les 20' sont finies]
                Si alpha < B: [barré pdt questions, alpha > B]
                    renvoyer alpha
                renvoyer alpha
            [


## Questions :
Q : on prend quoi pour A,B à l'init ?
R: des infinis

Q : []
R : oui mais les A, B sont les contraintes fournies par l'appel en haut

Q : Sur la feuille 42, avec les contraintes [A;B] = [0;15] ça donne quoi ?
R: oui ça retourne 42 la spec est pas bonne
Q : c'est gênant que la spec soit pas bonne ?
R: Non en fait AlphaBeta le but c'est d'approcher [NdManet le terme est pas forcément celui de Jules] les résultats
Q : Vos pouvez montrer sur un exemple quand ça évite des calculs ?
R : [s'exécute] Oui telle que je l'ai écrite ma spec est vraiment pas bonne
Q : je vois pas pourquoi ça évite le calcul, il y a un "pour chaque enfant e de a"...
R : Oui, je m'autorise une sortie anticipée de ma fonction donc de ma boucle

Q : Il termine votre algo ?
R : Oui si je corrige une typo

Q : C'est important d'avoir un arbre plutôt qu'un graphe ? 
R : Oui parce que éviter un bout de calcul n'est possible que pour une branche donnée, la borne trouvée n'est peut-être pas suffisante en passsant par ailleurs

Q : 
R : Aux échecs, si on a 20 coups à chaque fois, on doit estimer au lieu de
En moyenne en pratique, alpha-bêta permet d'explorer deux fois plus profondément 
Q : Il y a peut-être mieux aux échecs ?
R: Oui aux échecs c'est pas ultra adapté, on a l'heuristique du nombre de pièce pour approcher les valeurs de 1,0,-1 ou plutôt +\inf, 0, -\inf

Plan
Q : Vous avez parlé de [], est-ce que vous voyez d'autres méthodes qui peuvent être utiles ?
R : Euh... Non. 
RJury : les algo probabiliste : vous avez des  exemples ?
R : Tri rapide, avec choix du pivot. En IA : descente de gradient stochastique

Q : Pour la force brute, est-ce que dans le futur, il y aura des nouvelles solutions ?
R : Oui, avec les ordinateurs quantiques
Q : Vous avez une idée du gain ?
R : Log ?
RJury : plutôt racine 

Q : Entre les approches top-down et bottom-up en prog dyn, laquelle est mieux ?
R : En mémoïsation, si on ne sait pas quelles valeurs vont être utiles, on les découvrira au fur et à mesure
En [propagation], on économise de la mémoire. [NdManet et des appels de fonction]

Q : J'ai un problème, comment je détermine quelle stratégie je dois prendre ?
on pourra trouver des idées simillaires
Q : Oui, dans votre explication,
R : Alors oui, déjà ces stratégies ne sont pas mutuellement exclusives [exemple sur DPR]. Là je décris des idées, mais chaque problème, on voit pas les données [blabla]
R : oui, quand on fait un truc concrets c'est différent. un exemple : en algos de graphe, selon la rpzt du graphe (matrice/liste d'adj) on n'aura pas les mêmes algos

Q : [...] approximation ?
R : Si on accepte les solutions approchées, on peut relâcher un peu l'exploration pour gagner en efficacité.


## Remarques :

[RdFanny ] En vrai appelle les Alice et Bob, ça fait moins sens mais tu galères [Manet] jsp moi je galèrerai aussi entre les deux 
[RdManet : avoir cinq variables d'une lettre dont a, \alpha, A, B, \beta c'est galère à lire, surtout pour un truc aussi casse-gueule]
Rq : Attention à la phrase de conclusion : c'est mieux si elle existe

Rq : Vos choix de notation vous aident pas 
Jules : oui parfois c'était un peu ridicule
RJury : boah, c'était marrant

Rq : Le dessin de l'arbre c'était long, ça risque de perdre tout le monde dès le début
Il aurait fallu expliquer la construction de l'arbre 

Rq : votre définition c'est sur des jeux finis, il aurait fallu le dire. Attention aux questions sur les jeux auxquelles vous vous exposez

Rq : Il manque l'idée de la preuve. Ça aurait aidé sur la question de ce qu'il se passe quand on a un DAG au lieu d'un arbre, les infos qu'il faut garder

Rq : A* en objet c'est pratique
