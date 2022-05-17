# 21/04 - 20. Principes de fonctionnement des ordinateurs : architecture, notions d'assembleur - Yaëlle #

Développements :

- **Analyse de code assembleur [Choisi par le jury]**

- Construction du chemin de données en fonction des instructions



## Développement ##

[exécution du code à la main]



Qu'est-ce qu'on a fait ?

Première fonction : regarde deux entiers a0 et a1 et met le minimum des deux dans a0

Boucle L2 : TantQue s3 != s2,

or s3 va être un compteur, s2 initialisé à une taille (*8 pour la taille d'entiers) donc

Boucle L2 : TantQue compteur < size

   * Parcourt le tableau, trouve le minimum du tableau


C'est comme ça qu'on regarde du code assembleur à la main. Il y a des outils pour faire ça plus facilement.





Comment on produit du code assembleur [à partir du code machine] ?

000100010000 00000 000 01000 0010011

Opcode 0010011 donc de type i,

donc immédiat 000100010000 = 0x110

rs1 : 00000 = 0

rcl : 01000 = 16

funct3 : 000 soit addi

Donc c'est : addi x16, x0, 0x110



0000000 10011 01000 000 10100 0110011

Opcode 0110011 donc de type r,

donc deux sources

rs1 : 01000 = 8

rs2 : 10011 = 19

funct7 : 0

funct3 : 0

rd : 10100 = 20

soit add x20, x19, x8





## Questions/Remarques ##



### Développement ###

Q : Pourquoi utiliser muli pour multiplier par 8 ?

R : Parce que (rires) j'ai pas pensé à utiliser un shift par 3

RqManet : en vrai pour présenter du code aux élèves je suis pas du tout d'accord :o

RqAxel : C'est l'agreg, c'est pas fait pour les élèves



Q : Est-ce toujours facile de passer de l'assembleur au binaire ?

R : Non, en RISC-V déjà c'est plus facile parce que les instructions sont de taille fixe mais c'est pas forcément le cas

RJury : En vrai c'est possible de faire du jump non-aligné, qui fait que le désassemblage peut dépendre de la sémantique...

Plus les sauts dynamiques dont on ne sait pas où ils vont => difficulté de reconstruire le CFG



### Plan ###

Q : Vous n'avez pas du tout évoqué la notion de CISC et de RISC, est-ce que ca vous parait important, est-ce qui ca a in impact ?

R : Si vous avez un RISC c'est plus facile de construire un processeur et à manipuler.

RJury1 : oui un CISC il y a moins de régularité (la fonction de décodage est réentrante, donc notamment c'est limitant dans le pipelining

RJury2 : pas que, [...]



Q: En termes de consommation d'énergie, il vaut mieux avoir du CISK, du RISK, ou..?

R : Jsp

RJury : Jsp non plus



Q : on peut pas exécuter du MIPS sur du ARM ?

R : Non

RJury : Non mais il existe des mécanismes de traduction à la volée



Q : Dans le jeu d'instruction, quand on arrive aux fonctions, qu'est-ce qui dépend de l'archi et qu'est-ce qui n'en dépend pas ?

R : C'est l'archi qui définit les conventions d'appels (ex : en RISC, registres, en x86 sur la pile). Les registres sauvegardés par l'appelant et l'appelé dépendent aussi de l'architecture.

Q : à quoi ça sert les conventions d'appel ?

R : Ça sert à passer la main aux autres programmes

RqJury : la seule convention de stockage imposée (et non contournable par le logiciel) est le jal qui écrit l'adresse de retour dans un registre particulier.



## Remarques ##

### Plan ###

Rq : Il faut être précis : PC est un registre contenant l'adresse de l'instruction.



Rq : Vous ne parlez pas du chargement du programme



Rq : Vous n'avez pas du tout parlé de syscall, c'est un choix ? Il n'y a rien non plus sur le chargement du programme.







### Développement ###



Rq : il faut souligner que même si on optimise souvent les variables locales dans des registres, de base c'est censé être en mémoire, et en présenter ça aurait pu être bien



Rq : Peut-être que ce serait plus fluide de commencer par la traduction binaire->assembleur PUIS de l'exécuter à la main
