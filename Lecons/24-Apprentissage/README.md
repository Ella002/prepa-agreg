# 24 - Exemples d’algorithmes d’apprentissage supervisés et non supervisés. #

## Version Hugo ##

### Sources ###

???

### [Notes](notesHM.md) ###

### Plan ###

[Plan détaillé](planHM.pdf)

1. Apprentissage supervisé: exemple de l'algo k-NN
   1. Problème d'apprentissage supervisé: formalisation
   2. k-plus proches voisins
   3. Cas euclidien: accélération par K-d tree
2. Apprentissage non supervisé: clustering, k-moyennes
   1. Clustering: principe, applications
   2. Problème des k-moyennes
   3. Résolution de Lloyd
	  * Dev 1 = initialisation k-means++, preuve facteur approx
3. Evaluation et biais
   1. Evaluation, cross-validation
   2. Biais statistique, sur-apprentissage
   3. Propriétés des modèles
	  * Dev 2 = propriétés de k-nn euclidiens et des SVM: exploration avec scikit-learn
   4. Biais d'échantillonnage, biais sociaux

### Développements ###

- Dev 1 : initialisation k-means++, preuve facteur approx
- Dev 2 : propriétés de k-nn euclidiens et des SVM: exploration avec scikit-learn
  [Notebook Jupyter](HM-eval_KNN_SVM.ipynb)
