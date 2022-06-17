# 23/05 - 3. Tests de programme et inspection de code. - Jules #

Candidat : Jules Saget

Jury : Sylvain Schmitz, Jean-Jacques Levy



Plan :

1) Inspection de code

2) Tests de programme

## Développement ##

Test par chemins

Graphe de flot de contrôle (sommets = instructions, arêtes = transitions possibles)

Principes :

- soit passer par chaque sommet

- soit passer par chaque arête (différent, notamment pour if sans else)

- soit pour chaque raison pour laquelle une condition peut être vraie

- soit pour chaque chemin possible (pas réaliste en pratique)



On va illustrer ça sur un programme bogué.



[dessine le graphe de flot de contrôle de dev2.py]

Illustre les quatre stratégies qui, chacune leur tour, permettent d'identifier des erreurs





## Questions ##

### Dev ###

Q : Comment tu vérifies par où tu es passé ?

R : À la main. Je ne résouds pas, ici, le problème de couverture de code, qui est indécidable en générale



Q : [Analyses plus statiques ?]

R : [...]



Q : Il y a une communauté qui essaye de générer des jeux de tests. Vous savez comment iels font.

R : Oui, par exemple :

- [structure de la chaine de caractères]

- sort de Python se comporte différemment en fonction de taille, etc. On peut analyser ça statiquement [NDLR pas sûr de ce que j'ai entendu ?] et s'en servir



Q : C'est pas de l'analyse un peu statique quand même ?

R : Si, mais avec pour objectif de guider un testing



Q : Les méthodes formelles c'est utilisé en industrie ?

R : Oui (métro, Astrée...)

Après c'est pas super courant parce que ça nécessite une vrai expertise mathématique



Q : Vous avez pas parlé de concurrence ?

R : Un peu, si, dans la partie "message passing"

Et je sais pas si les méthodes utilisées sont fondamentalement différentes.



## Remarques ##

### Devt ###

Schmitz : C'est bien de présenter les flots de contrôle, mais c'est peut-être un peu trop complexe ?

R : Oui mais j'ai pas trouvé plus compact



Levy : toujours mieux de commencer par dessiner avant de montrer du code

R : oui



Schmitz : c'est quoi tes refs ?

R : Pour les devts, pas de réf. Le plan c'est [...] c'est pour ça qu'on n'a pas



Levy : Pour les [...] il y a des trucs très sophistiqués, et qui marchent ! et qui marchent !

R : ...



### Plan ###

Schmitz : très bien. Le Devt1 est peut-être trop formel en comparaison

Levy : oui, plan très bien. Le Devt1 est, pour la communauté française, très très classique, peut-être trop ?
