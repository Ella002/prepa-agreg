# Approximation de droites #
## Sujet agreg math, option info, 2012 ##

[Sujet](Sujet.pdf)

### Aurore 🌅 ###

#### Plan 🗺️ ####

   1. Introduction
   1. Algorithmes 🖥️
       1. Bresenham
       1. Plus proche inférieurement
   1. Mots associés à une droite ↗️


#### Questions ❔ ####

❔ Intérêt de l'algo de Bresenham ?

➡️ Efficace (linéaire), ne manipule que des entiers



❔ Algorithmes similaires (pour représenter un cercle par ex)

➡️ Repère en (x, y) pas forcément très pratique mais en parcourant circulairement on doit pouvoir adapter l'algo



❔ Pourquoi demander que la pente soit inférieure à 1

➡️ Pour borner l'erreur, toujours moins de m/2 donc avec m = 1 on a une erreur d'au plus 1/2. Si la pente est supérieure à 1, il y a un trop gros trou entre deux points. On peut alors échanger les rôles de x et y pour se ramener au cas pente < 1.



❔ Comment formaliser cette notion ?

➡️ Notion de 8-connexité (définie dans le sujet)



#### Remarques 📝 ####



📝 Insister sur l'utilisation des entiers dans Bresenham dès la présentation

📝 Bien préparer la preuve. En cas de doute, mieux vaut continuer à recopier son brouillon en annonçant qu'il y a (peut-être) un problème plutôt que de perdre du temps à déboguer.

📝 Parler vite 🏎️💨 : mieux vaut finir en avance que de meubler 🛋️ (le jury s'en rend compte...)

📝 On peut abréger une preuve : énoncer rapidement mais précisément les étapes de la preuve, sans rentrer dans les détails mais pas en le faisant vite fait avec les mains

📝 Ne pas faire trop de preuves

📝 Manque un peu la partie recul sur le modèle



### Axel 🪓🇱 ###


#### Plan 🗺️ ####

   1. Représentation de segments
       1. Nuage de points au plus près inférieurement
       1. Algorithme de Bresenham
   1. Droites discrètes et encodage de rationnels
       1. Définitions
       1. Périodicité du mot binaire associé
       1. Changement d'ordonnée à l'origine
       1. Lien avec les rationnels


#### Questions ❔ ####



❔ Pourquoi avoir modifié l'algo de Bresenham ?

➡️ Pour être cohérent avec la suite du sujet



❔ Comment gérer une pente >= 1 ?

➡️ On fait avancer les y



#### Remarques 📝 ####



📝 Dépassement de 5 minutes : c'est **beaucoup trop** !

    📝 Pour le programme : KISS. Pas la peine de faire une classe (qui introduit des constructions lourdes comme self à chaque fonction) pour un programme si court

📝 Faire des illustrations dès le début
