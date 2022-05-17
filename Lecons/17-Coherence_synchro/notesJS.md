# 07/04 - 17. Problèmes et stratégies de synchronisation et de cohérence - Jules



**Développements**

- **Boulangerie de Lamport <-- choisi par le jury**

- Preuve du théorème: Primitives RMW \in Common2 -> numéro de consensus 2



## Développement



Procédure d'exclusion mutuelle pour un nombre n de processus



Principe : chaque processus prend un ticket, et les tickets sont résolus dans l'ordre. PB : la prise de tickets est concurrente, donc peut ne pas être injective... On départagera avec le numéro de processus.





### Algorithme


```
n processus p\_0, ..., p\_{n-1}

label[n] atomiques entiers

flag[n] atomiques booléens
```


*Section d'entrée de p\_i*

```
// p\_i lève le drapeau

    flag[i] = 1

    // prise d'un ticket

    l = max (label[0], ..., label[n-1]) + 1

    label[i] = l



    // p\_i attend son tour

    TantQue(\exists k \neq i, flag[k] == i

           * \and (label[k],k) <\_{lex} (label[i], i) )
   * Attendre
```

*Section de sortie de p\_i*


```
// p\_i baisse le drapeau

    flag[i] = 0
```


*Configuration initiale*



tous les flags à 0, label à 0





### Preuve de (1 = exclusion mutuelle)



Supposons qu'on aie p\_i et p\_j (i \neq j) en section critique

Sq (label[i], i) <lex (label[j], j)



Au moment de la vérification [oral : de la fin du TantQue] de p\_j :

   * soit flag[i] = 0: impossible, sinon p\_i ne serait pas en section critique
   * soit label[j] < label[i]: impossible, les labels ne font qu'augmenter, j n'a pas pu modifier son label pour qu'il devienne plus petit
   * soit label[j] == label[i] et j < i: impossible, i et j n'ont pas changé


CQFD: l'algo de la boulangerie de Lamport satisfait bien l'exclusion mutuelle



### Preuve de (2 = pas de blocage)



On va montrer qu'il n'y a pas de blocage, puis que l'algorithme suit le principe "premier arrivé, premier servi".



Blocage = il y a des processus en section d'entrée, et à tout moment dans le futur il n'y aura aucun processus en section critique.



Parmi tous les processeurs en entrée, il existe p\_i qui minimise (label[i], i), donc p\_i va finir par entrer en SC.



### Propriété (4) [rajoutée au tableau, pas dans le plan]

Si p\_i est dans sa phase d'attente et p\_j rentre en section d'entrée, alors p\_i atteindra sa SC avant p\_j.



### (4) \&\& (2) => (3)



p\_i en section d'entrée

On a k processus p\_i\_0, ..., p\_i\_{k-1} qui sont en section d'entrée après un instant t donné pendant l'attente de p\_i.

De par la propriété (2), un de ces processus (p\_l) va passer en section critique. Si c'est p\_i, c'est gagné. Sinon, on élimine les processus d'indice < l, par (4), et on recommence.

Par récurrence, p\_i entrera en SC le k-ème, dans le pire des cas.



## Questions



### Développement



Q: Le max() est pas atomique mais on voit comment le faire. Mais comment vous faites "tant que il existe"?

R: le nombre de processus est fixé à l'avance, donc on peut faire un gros OU avec les n processus. Alternativement, une boucle for pour parcourir tous les processus et vérifier si la condition est vraie.



Q: pourquoi avoir change l'ordre entre l'attribution du label et le lever de drapeau? [NdY: Jules est revenu en arrière pour modifier le début de la section d'entrée]

R: on aura un premier processus qui prend son label (ex label[0] = 1) puis attend avant le lever de drapeau ;

un autre processus fait la même chose en même temps (ex label[1] = 1) puis passe devant

et ensuite les deux passent le test dans le bon ordre et font leur SC en même temps

Q: et donc là, pourquoi un booléen est suffisant? On aurait pu s'attendre à ce que ce soit plus qu'un booléen le... (flag?)

R: si on n'a pas de critère d'admissibilité, ie on suppose qu'un processus peut planter: quand un processus qui a un petit label lève son drapeau et plante, ça bloque tout le monde. Ici on a supposé que les processus ne plantaient pas, donc c'est ok.



Q : est ce que avec les architecture actuelles le fait que l'ordre d'exécution des instructions soit perturbé pose problème ?

R: Je suppose que non mais je m'y connais pas, il y a peut-être aussi des garanties qui font que en pratique on peut considérer que oui. (NdF : faut peut etre echanger le oui et le non dans la réponse, j'ai pas compris)



Q: en pratique, si l'algo de la boulangerie ne fonctionne pas (surtout qu'il y a une hypothèse forte: on connait le nombre de processus), qu'est-ce qu'on peut faire?

R: jsp comment fonctionnent les mutex de pthread sous le capot.

Hypothèse: y a un système d'élection de chef

Je suppose qu'on doit pouvoir briser les symétries grâce au numéro de processus



Q: Sur la notion d'admissibilité, vous n'autorisez pas les crashs dans la partie reste ?

R: tel que je l'ai défini, non. Mais ça ne poserait pas de problème, a priori. Pour les autres c'est comme s'il faisait une boucle infinie sans rentrer en section critique [ndManet : ni d'entrée].



### Plan



Q: qu'est-ce que ça veut dire une primitive forte?

R: forte/faible ce n'est pas formellement défini, mais ça vient du fait que l'algo d'exclusion mutuelle avec test and set fait une ligne, alors que si on a juste read et write il faut faire des choses compliquées.

Au sens du numéro de consensus, test and set est plus fort que read and write



Q: pourquoi famine c'est pas bien? [pourquoi c'est barré sur le plan ?]

R: à la base je m'étais mélangé et j'avais confondu les notions de famine et recalage, mais en fait c'est deux choses différentes et recalage n'a de sens que dans le contexte de l'exclusion mutuelle alors que famine c'est plus général

la famine c'est à peu près que même si les autres processus crashent celui-là peut continuer son travail.

recalage c'est une traduction Jules:tm: de lockout



Q: Pour l'algo proposé avec test\&set, il manque une hypothèse pour avoir la propriété (3) ?

R: en effet, il y a pas de raison de croire qu'un processus va finir par passer

Q: quelle hypothèse rajouter?

R: premier arrivé premier servi?

Q: il manque des infos sur la primitive attente. Active, passive?

R: active

Q: dans ce cas il manque une hypothèse pour (3)



Q (Lejeune): niveau système, si on fait une attente active c'est pas trivial. Si c'est une attente passive...

R: L'attente passive on demande à l'OS de nous réveiller, il y a un leader [NdY: \o/ .o. \o/]

Le modèle où je me place est a priori symétrique

Si on suppose qu'il y a un OS qui rappellera les gens dans l'ordre auquel ils ont fait appel à test and set, la propriété (3) est vérifiée

Ces réflexions peuvent se porter à plusieurs machines communiquant via broadcast

[RqDFHourlin : oui c'est très pertinent dans le big data], pas seulement à des processus au sein d'une machine. Et dans ce cas on est obligé de faire de l'attente active





Q: comment on généralise Peterson à plus de 2?

R: On va faire une tour [prend une craie, dessine un truc, l'efface, sur un ton hésitant : ]

On va faire un tournoi: p0 et p1 s'affrontent via verrou, ainsi que p2 et p3, puis les deux gagnants.

Q: Si on fait ça qu'est-ce qu'on garde des propriétés (1) (2) (3) ?

R: Je crois qu'on garde (1) et (2) mais pas (3).

On a aussi un modèle par étages : A chaque étage on se bat pour atteindre l'étage d'en-dessous, on garantit qu'il y a un seul processus qui descend à chaque étape, et au dernier étage c'est la SC.

Q: et du coup ?

R: je crois qu'on a aussi le (3)



Q: est-ce qu'il peut y avoir des cas dans la vie où ne pas avoir (2) et (3) n'est pas forcément respecté ? Disons que (3)

R: (3) c'est pas très grave dans un contexte où tous les processeurs vont terminer -> (3) est respecté. Ou si on n'a pas beaucoup de proc, et/ou que c'est rare que beaucoup de proc veulent rentrer en même temps.

L'avantage c'est que si on l'a on est sûr·e·s que ça marchera.



Q: ça manque de cohérence (au sens où le titre c'est cohérence et synchronisation), que pouvez vous nous en dire?

R: Yep.

Une définition informelle, par exemple dans une BDD distribuée, deux ordis différents soient d'accord sur une valeur de la BDD.

Par exemple la blockchain [haha ce namedropping]



Q: Par exemple, sur une BDD, on voudrait que deux requêtes similaires aient la même réponse ?

R: Oui, c'est souhaitable, mais pas toujours vrai. Important pour des données médicales, pas pour un nombre de likes



Q: Def du consensus ?

R: [...]

Q: À quoi ça sert ?

R: C'est surtout vu comme un outil théorique.

On peut aussi avoir envie d'un consensus "démocratique",





[AFK batterie incoming. Promis, je le fais pas exprès]



Q: toutes les définitions, elles sont issues de livre ou...?

R: Oui c'est issu de livres, avec traduction Jules:tm: parce que les livres sont en anglais

The Art of Multiprocessor Programming et [...]











## Remarques



RqDYaëlle: processus ou processeurs? ^^"



RqDMourlin: regardez le(s) livre(s) de Joffroy Beauquier [NdY: il est très très fan de Beauquier ce monsieur XD]



RqDMourlin: dommage de ne pas utiliser le tableau, et les hésitations ont rendu plus compliqué de suivre



### Plan



RqDH : c'était agréable



RqDManet : Peut-être rappeler la déf d'opération atomique, dans le cadre de la modélisation (ie qu'est-ce qui se passe précisément si deux processeurs exécutent la même primitive atomique ?)



RqDMourlin: vous parlez de blockchain pour parler de cohérence, c'est peut-être plus facile de parler de PageRank qui est plus courant et facile à expliquer



RqDFr : insister un peu plus sur l'atomicité et []



RqDFr : Ecrire l'algo du dev dans le plan, gagne du temps et de l'énergie pour le devpt

[RqDManet : je suis pas convaincu][RqdF : si t'as la place, je pense que c'est une bonne idée, sinon bof]



RqDLejeune : présenter différentes notions de cohérence ("stratégies" est au pluriel)[RqDFanny : théorique s'oppose à informatique ???? [RqDManet : vu l'agreg, il semble que oui] 😭 ]



Rq: Par exemple on peut aussi parler de sémaphore



Rq: on peut aussi parler d'interblocages (dîners de philosophes, etc)



Rq : la cohérence ne se résume pas au consensus



RqDLJ : en vrai les registres il y en a dans le processus, là vous les cachez dans l'état...

R : oui j'ai essayé d'abstraire

RqDLJ : ouais, c'est valide, mais il faudrait essayer de plus faire le lien entre théorie et pratique



### Développement

RqDFanny : Essayer de pas se mettre devant ce qu'on écrit, et éviter de parler au tableau + Ecrire les titres de parties au tableau (genre écrire : preuve d'absence de blocage, plutôt que preuve de (2)) + 1



RqDFr: 20 minutes pour présenter l'algo et faire les 3 bouts de preuve c'est ambitieux
