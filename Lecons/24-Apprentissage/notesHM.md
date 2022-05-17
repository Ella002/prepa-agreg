# 05-10 - 24. Exemples d’algorithmes d’apprentissage supervisés et non supervisés - Hugo #



Serge Haddad et Marc Lelarge



Développements:

   * Preuve de l'initialisation k-means ++
   * Propriétés de k-NN euclidien et SVM (support vector machine) : utilisation d'une bibliothèque python (sklearn / scikit-learn) **<-- Choisi par le jury**


## Développement ##



Contexte: on vient de parler de biais statistique et de sur-apprentissage, maintenant on va faire un TP là-dessus



On utilise scikit-learn, et l'ensemble de données "iris", fourni



Présentation k-plus proches voisins. On peut dessiner les frontières des espaces de décision pour 15 plus proches voisins

-> résultat "idéal"



Introduction des machines à vecteur de support



Avantage: pré-calcul des fonctions de écision, mais apres rapide de déterminer 'hyperplan auqleu appartient un point



A la fin, introduction d'un set de données à 4 paramètres, et démonstration des résultats des deux



## Questions ##



QML : Vous avez classé ce développement dans la section propriété des modèles. Quelles propriétés des modèles est-ce que vous explorez ?

R : Compliqué à classer dans une partie, surtout variance par mise à l'échelle sur une dimension

QML : Donc c'est une propriété de non invariance de KNN par mise à l'échelle



Q : Surapprentissage ?

R : Sur le graphe "ideal" où on a 100% de succès sur le test, on a des frontières complexes, qui résultent de surapprentissage.



Q : Donc chaque point est un échantillon, et sa couleur est sa classe ? A quoi correspondent les couleurs de fond

R : Oui, et le fond c'est la réponse du classifieur

Q : Donc il y a pas de train et de test ? Il faut le dire ! Pourquoi ce choix ?

R : Oui. Je n'ai pas besoin de séparation parce que je regarde les effets de biais des algorithmes.



Q : Pourquoi il y a des iles de bleu dans la zone jaune ?

R : Parce qu'on a une concentration locale de bleus dans l'océan de jaune, ce que fait que pour certains points les plus proches voisins seront bleus. Ca se corrige en prenant plus de voisins. PAr exemple, si on réduit le nombre de voisins à 3 dans l'exemple, les frontières deviennent encore plus arbitraires.



Q : Tu as dis "c'est recommandé". Par qui, par quoi ? De même, tu as dis "c'est idéal", pourquoi ?

R : Ca m'a échappé. Je pense que c'est parce que ce jeu de données, même avec des classifieurs assez simples on a de très bons résultats.



Q : A quoi correspondent les chiffres à la fin ? Pourquoi l'un est meilleur que l'autre ?

Rq : Il faut expliquer la mesure de performance, le vecteur permet d'expliquer la validation croisée.



Q : L'alternance entre association de centre et affectation des points au centre, ca te fait penser à d'autres algos ? Proceeds to donner un type d'algo qu'on pourrait avoir en développement.

[C'était Expectation-Maximization]



## Remarques ##

RqML : Il faudrait présenter Jupyter et sklearn. Utilisez aussi la puissance de Jupyter pour intercaler du Latex avec le code. Indépendamment des outils, il faut présenter le dataset (nombre d'exemple, labels, données).

TLDR: ne pas foncer dans le code, prendre le temps de présenter ce qu'on manipule



RqML: il faut mentionner la mesure de précision



RqML: SVM, [RdY: j'entends pas ce qu'il dit]



Rq : il manque la différence entre apprentissage supervisé, et non supervisé. Il faut faire attention à différencier le problème, les méthodes et les algorithmes. Il faut parler de la séparation train/validation/test



RqSH: très bien de faire une intro, mais il faut que le lien soit évident [RqAxel : ON VOUS A MENTI] [RqSH : quand tu commences à réfléchir, tu utilises des mots plus pertinents que ceux que tu as écrits #burn]



Rq : Mettre des trucs de la partie 3 avant dans le plan, mettre validation croisée à la fin
