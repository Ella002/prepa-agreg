# 13/06 - 14. Gestion et coordination de multiples fils d’exécution - Fanny #

## Plan ##



## Développement ##

- Boulangerie de Lamport
- **Dîner des philosophes** (choisi par le jury)

N philosophes sur une table circulaire, avec 1 fourchette entre chaque paire de philosophes, et besoin des deux fourchettes pour manger.


Possibilité de blocage si chaque philosophe prend la fourchette à sa droite
[note à l'oral : Par exemple,  si chaque philosophe exécute le programme simple :
```
Boucle :
    réfléchit()
    prend_fourchette_droite()
    prend_fourchette_gauche()
    mange()
    relache_fourchette_droite()
    relache_fourchette_gauche()
```
alors il peut y avoir ce blocage]

```
état[N] : 0 <- réfléchit ;

        1  <- a faim ;

        2 <- mange.
```

mutex `exclusion` : pour modif état, donc 1 seul peut changer à la fois

sémaphore aut[i]  : autorisation de manger

Quand un philosophe a faim :
```
exclusion.lock()

etat[i] := 1

if etat[(i - 1) % N] \neq 2 et etat[(i + 1) % N] \neq 2

    etat[i] := 2 <- réserver les fourchettes

    aut[i].augmenter()

exclusion.unlock()

aut[i].diminuer()

manger()
```

Finit de manger : [oral : je débloque les fourchetttes. peut-être que du coup mes voisins sont débloqués
```
exclusion.lock()
etat[i] := 0
if etat[(i - 1) % N] = 1 et etat[(i - 2) % N] \neq 2 :
    etat[(i - 1) % N] = 2
    aut[(i - 1) % N].augmente()
if ______ i + 1 ________ [idem que le if précédent]

exclusion.unlock()
réfléchir()
```

Mais ça résoud pas tous les problèmes.
famine : un philosophe ne mange jamais.
[dessin où à chaque instant le philosophe 1 ou 3 est en train de manger]
Une solution : Boulangerie de Lamport où un seul philosophe mange à la fois


## Questions ##
Q : La boulangerie de Lamport c'est la seule solution ?
R : Probablement pas mais pour l'instant j'en vois pas

Q : c'est pas bizarre de mettre les sémaphores sur les philosophes au lieu des fourchettes ?
RJury : les sémaphores sur les fourchettes ça marche aussi

Q : Autre terme pour exclusion mutuelle, hors mutex et sémaphore ?
R : Registre [Test and set ?]
Rq : Fonction qui marche sur deux trucs...

Q: Vous avez défini une solution sans interblocage. Vous pouvez prouver pourquoi cette solution l'est ?
R : Il faut étudier un état du système dans lequel il y a un philosophe dans l'état 1 et il y aura dans le future un philosophe dans l'état 2.
S'il y n'y en a pas à un instant où on veut manger, alors on mange donc OK. Sinon, quelqu'un mange.
Un invariant qu'on peut vouloir prouver c'est [...] et ça a priori ça suffit.

### Plan ###
Q : En pratique si je veux créer des processus ou des fils d'executions en C comment je fais ?
R : Il y a des bibliothèques pour des threads
Q : Et si j'ai juste des boucles que je veux paralléliser, vous connaissez des bibliothèques plus simples ? OpenMP par exemple ?
R : Non

Q : Et si je veux des processus plutôt que des fils ?
R : fork(), exec()
Q : Intérêt des threads plutôt que processus ?
R : Mémoire partagée, commutation moins coûteuse

Q : C'est coûteux les changements de contexte ?
R : Tout dépend du temps d'exécution qu'on laisse entre les commutations

Q : Vous avez introduit l'exécution mutuelle sur un exemple. Comment on peut juger si un ordonnancement est correct ?
R : En pratique, mettre mutex et sémaphore pour éviter mauvais ordonnancements.
Il y a un problème si l'ordonnancement change le résultat donné
Q : Change le résultat par rapport à quoi ? C'est quoi votre standard ?
R : En fait un algo est bon s'il ne dépend pas de l'ordonnancement

    Rq : Mais ça vous aurez des problèmes ne serait-ce que sur une somme de nombres flottaants

    R : Pas d'effet de bord dus aux autres threads peut-être ?

RJury : on peut par exemple considérer les ordonnancements sériels, et considérer qu'ils sont bons

Q : Différences entre Threads et processus ?
R : C'est un peu la même chose. Mais le thread est le fil de l'exécution, et le processus est un environnement de travail.
Q : Il y aune sorte de contenance ? De qui vers qui ?
R: Un fil est contenu dans un processus

Q : Partage de mémoire entre quoi et quoi ?
R : Il y a partage de mémoire entre threads d'un même processus.

Q : Entre processus, pas de partage de mémoire ?
R : Avec mémoire virtuelle, pas d'accès d'un processus à la mémoire d'un autre.
Q : Mais j'avais entendu parler de parallélisme par processus
R : oui mais ce serait par boite noire
Q: Moyen d'envoyer des messages entre processus ?
R : Par fichiers interposés.
Rq : Dans la bibliothèque MPI, il y a. Et les queues en Python.

Q : Il y a d'autres noms our les threads ?
R : on dit aussi "processus legers"


Q : Intel vendent aussi dans leurs processeurs de l'hyperthreading
R : Je sais pas ce que c'est.
RJury : Moi non plus [MDR]

## Remarques ##
Q : Y avait-il moyen de faire un programme d'illustration ?
R : Oui, mais faut voir le temps d'implémentation.
RqJules : Attention, Ocaml détecte l'interblocage et tue un fil.
RqManet : Pour le TP blanc ça m'avait pris des heures de faire fonctionner des threads basiques

Rq : On pourrait montrer que si on déplace les contraintes, on a une solution différente



Rq : Nous on est dans l'état 1. [a faim]
