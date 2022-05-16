# 19/04 - 16. Mémoire : du bit à l’abstraction vue par les processus. - Hector #

Stephane Rovedakis et Jonathan Lejeune



**Développements**

- Représentation des flottants (IEEE 754)

-** Ramasse-miettes** [RdY: j'adore ce nom français]  <- Choix du jury



## Développement ##

Hector en avait pas, mais dit qu'il aurait trouvé cool de faire un exemple avec du code C [RdY: je suis pas sûre qu'un exemple de code soit si judicieux]



Objectif: déterminer si on peut nettoyer une donnée de la mémoire



Est ce qu'une donnée aura une utilité dans le futur ? C'est un problème indécidable

=> on regarde si la donnée est accessible (en suivant les pointeurs)



### I. Comptage de références ###


```
    |----------|

    |          |←

    |          |  |

    |----------|  | 0 → 1 → 0

    |    X     | -

    |----------|

    |          |
```


-> Problèmes de cycles

-> Utilisation fichier

=> Ca ne marche pas /!\



### II. Marquer et balayer ###



On va faire plutôt des cycles de marquage :

-> Aucun objet noir ne référence un objet blanc

-> A chaque cycle, on part d'un objet gris, et on grise les objets auxquels il fait référence. L'objet de départ devient noir.

En partant de la racine, on a la liste des objets auquel une référence est faite



### III. Méthode opérationnelle ###



Idée: une donnée qui est là depuis longtemps va probablement rester longtemps, alors qu'un truc récent possiblement pas (ex: variable temporaire)



On va avoir plusieurs génération, à chaque fois qu'on balaye, si des données sont utilisées, on les envoie dans la génération suivante.



Beaucoup de paramètres pour fixer combien de temps avant de passer à la génération suivante, et combien de générations.



Python/CPython : 3

Ocaml : 2 zones de données / tas



Le comptage de références à l'avantage de libérer instantanément une variable non utilisée, contrairement à la dernière méthode présentée qui demande plusieurs cycles avant la libération.



## Questions ##



### Développement ###



QSR: On comprend que la problématique est la libération de la mémoire, mais à quel moment est ce qu'on active ces mécanismes ?

QSR: Quels sont les critères pour choisir telle ou telle méthode ?

R: C'est là qu'il y a une différence entre les méthodes: le comptage de référence doit être appliqué  chaque affectation, les autres son tappliquées à intervalle régulier, choisi de manière à ne pas passer trop de temps à ranger la mémoire



QSR: "On n'a pas trop de mémoire / pas suffisament de mémoire" ça veut dire quoi ?

R:  Objet de taille trop grande / tas qui n'a plus de place



QSR: Si on laisse de la fragmentation, à quoi ça va nous conduire ?

R: La mémoire fragmentée oblige que plus de choses à se souvenir pour accéder aux données / les regrouper => c'est une liste chaînée, on a un pointeur par fragment



QSR: Un peu annexe mais : Qu'est ce qu'il se passerait si une partie de la mémoire devenait dysfonctionnelle ? Comment s'en sortirait le système ?

R: On perdrait l'information "il y a un pointeur sur ce bloc", donc on risque de désallouer des variables qui étaient utiles.

Conclusion: si on n'a pas confiance en la mémoire, il faut faire beaucoup plus de choses pour s'assurer que tout va bien



QJL: Pourquoi on fait des ramasses-miettes et quel est leurs coût ?

R: Simplifie beaucoup la vie, garantis que l'on n'ait pas de fuite de mémoire. Les optimisations sont au bon vouloir du ramasse miettes (ce qui est une bonne chose, généralement). En fonction de si on veut beaucoup de performance ou au contraire du code plus simple a exprimer on va choisir ou non un langage avec un ramasse miettes.



QJL: En C par exemple, il n'y a donc pas de ramasses-miettes ?

R: Je crois qu'il y a une possiblité pour en faire un en C, en tout cas il y en a en C++. Il faut, pour faire un ramasse-miette, qu'on soit capable de vérifier si une variable accède ou non à une donnée. En C, il y a des destructeurs.



QJL: Tu as dit qu'avec une politique de pointeur, on ne peut pas faire de ramasse-miette, pourquoi ?

R: Si, on peut, je voulais dire qu'il faut alors délimiter une zone de données accessibles par des pointeur -> Problème de retour en arrière



QJL: En python, il n'y a pas de pointeur, qu'est ce qu'il y a et quelle est la différence avec un pointeur ?

R: On parle de référence, on ne peut alors pas ????



QJL: Qu'est ce qu'une racine et comment on peut les détecter ?

R: C'est une information donnée par le système qui signale quelles sont les données auxquelles on a accès au départ.

QJL: c'est le sustème, donc on est obligé de passer par le système?

R: à l'échelle du processus, il y a probablement des informations sur la pile



[ J'en ai marre d'eduroam qui me deco dès que j'écris un truc TT\_TT ]





QJL: Revenons à la fragmentation, est ce que la pagination (pour la mémoire virtuelle) peut limiter la fragmentation, ou est ce qu'elle l'aggrave ?

R: ça va dépendre de certaines circonstances. Si les pages sont trop grandes, ou chargées dans le mauvais ordre, on peut avoir des zones de mémoire inutilisées et d

QJL: Le but de la pagination est de découper la mémoire en morceau de manière à ce qu'on puisse utiliser la localité spatiale. Est-ce que ça n'atténue pas un peu ?

R: ça aide pour garder des grands espaces contigus libres mais ça n'empêche pas de re-déplacer les données en mémoire.

RqSR: Plus c'est fragmenté, plus il faudra des pages dans le cache, plus c'est contigu, moins on a de pages à ramener, plus c'est efficace.



QSR: par rapport au problème de pointeur, vous n'avez pas parler d'analyse du code. Impact sur le ramasse-miettes? Est-ce que lien entre code exécuté et ramasse-miettes? Est-ce que ramasse-miettes peut utiliser infos sur programme exécuté?

R: Comme c'est dynamique, on sait qu'on ne pourra pas avoir une solution qui marche à tous les coups. Sur les comptages de références, on sait qu'on a une fonction qui en appelle une autre puis qui renvoie qqch, on va augmenter puis diminuer le compteur de pointeur. Si on sait qu'on va revenir à zéro, on n'a pas besoin de rajouter et d'enlever 1.

RqSR: En effet, en analysant statiquement le code, on peut donc déterminer la portée d'une variable. On ne peut pas faire ça sans une analyse statique.



QJL: Comment ça se met en place un ramasse-miette, quel que soit l'algorithme derrière ?

R: A l’échelle du processus donc c'est le processus qui gère sa propre mémoire et se met en pause pour laisser la place du ramasse-miette. En cas de processus parallèles -> Problème de concurrence entre le ramasse-miette et le(s) processus parallèles.

QJL: C'est donc possible d'avoir un ramasse-miette et le processus qui s'éxécute en même temps ?

R: Je pense que c'est possible conceptuellement.

QJL: Donc le "quand" est décidé à l'avance ?

R: ???



### Plan ###



Q: Comment on retrouve l'impact des normes dans cette leçon? (notamment, le premier développement était une norme spécifique adaptée aux flottants)

R: Dans mon dev 1, c'est la norme la plus utilisée. 3C) pour codifier les processus pour qu'un objet est le même format pour tout le monde et garder une cohérence.

RqSR: Interopérabilité. Sans norme, beaucoup de problèmes d'accès aux données. Avoir une norme, c'est aussi structurer une donnée. Peut être mis en avant dans une partie du plan. Historiquement, beaucoup de soucis.



QSR: Vous parlez d'avoir plusieurs objets pour faire communiquer les processus entre eux, pourquoi plusieurs objets (tubes, files, ...) ?

R: Les processus sont tout puissant dans leur zone mémoire. Si deux processus accède à une même donnée, problème de concurrence. Il faut donc traiter ces conflits. Chaque objet a des propriétés particulières.



QSR: Si j'ai 10 processus lourds qui s’exécutent, j'ai une version avec des tubes et une version avec des files de messages, quelle(s) différence(s) ? Comme un espèce de bus de données où chaque processus va se connecter pour l'échange de données.

R: Avec des tubes : On essaye d'avoir un tube pour chaque connexion avec chaque client. Juste un tube => seul le premier client récupère le message.

RqSR: processus-serveurs, j'ai besoin de un seul tube, deux tubes ?

R: Deux tubes car sinon il est possible que le processus récupère son propre message.

R: Files de messages -> bidirectionnel. Par contre, on peut retrouver la même problématique.



QJL: Peux-tu développer la partir 3A ?

R: Unité de gestion de la mémoire permet de manipuler la mémoire plus facilement. A chaque fois qu'on commute, il faut renouveler les information de l'adresse de la table des pages souhaitée.

QJL: Dans quel cas on a besoin de demander une adresse virtuelle directement à partir d'une adresse physique.

R: Le processus manipule des adresses virtuelles.

QJL: Dans quel cas on manipule des adresses physiques et pourquoi on aurait besoin de la convertir en adresse physique ?

QSR: Où est stockée la table des pages ?

R: Dans la mémoire

QJL: C'est un segment propre à l'OS ou par le processus ?

R: Il faut passer par l'OS.

QJL: L'OS maintient une table des pages pour tous les processus ou par processus ?

R: Une table par processus.



QJL: Au début, tu as dit différence entre octet et byte, c'est quoi ?

R: Dans la pratique, pas de différence. Octet = unité. Byte ne correspond pas toujours à un octet, mais en pratique c'est souvent le cas.



QJL: Est-ce qu'on aurait pu utiliser une base 10 au lieu d'une base 2 en informatique ?

R: Raison physique, si on a du courant qui passe ou qui ne passe pas, c'est facile, sinon, pour une base plus grande, il faudrait jouer sur des variation de tension, plus prompt aux erreurs.



## Remarques ##



RqSR: Il faut bien préciser que si on a plusieurs outils de communication entre les processus, ce n'est pas pour rien, il faut expliquer pourquoi !



RqJL: Mémoire morte est non volatile et immuable. Disque est non volatile et mutable. Mémoire morte = ROM. L'un c'est accès direct à l'octet, l'autre est read-only. Disque = accès par blocs, non volatile mais read-write.



RqSR: la structure générale du plan est correcte, mais il faut mieux éclairer certaines parties. Pourquoi le binaire (plus facile à diffŕencier dans le stockage électrique)? Parler de hiérarchie mémoire, importante dans la différentiation des niveaux de mémoire. Les normes.



RqJL: Arbre = structure de donnée, ce n'est pas la mémoire, c'est une utilisation de la mémoire.



Rq: discussion sur la mémoire virtuelle, comment ça fonctionne et à quoi ça sert



RqJL: Il manque un point sur l'allocation de la mémoire avant le ramasse-miette.



[décrochage général de la team notes] Yep



RqJL: surpris par le choix du ramasse-miettes, parce qu'il faut aussi un runtime. Par contre, ça pourrait être une ouverture.

RqSR : On aurait pu, en second développement, discuter des moyens de communication entre les processus.



RqJL: certaines réponses confuses / pas précises. Ça se sentait que c'était préparé au dernier moment



RqJL: Il faut utiliser les termes précis lorsqu'on parle de quelque chose.



RqJL: il vaut mieux reconnaître qu'on ne sait pas, plutôt que faire une réponse bancale



Conclusion: la structure est là, il faut le bosser pour être plus punchy



Suggestion: on fait un développement sur une méthode. Par exemple, pour la concurrence: "étant donnés des primitives de mutex, comment on construit un sémaphore?"



Remarque globale sur le plan:

Sur le fond, le plan est bon. Il faudrait rajouter allocation / désallocation de la mémoire dans la partie 3, et motiver (hiérarchie)

Exemple développement: algorithme allocation mémoire OS
