# Quelques retours sur la leçon "Requêtes en Langage SQL"


9 décembre 2021

Etudiant: Thomas Magnard

Enseignant: Bernd AMANN

## Plan de leçon:

La structure du plan général est bien. 

Suggestions: 

- montrer un exemple de schéma E/A et sa traduction relationnel au début et utiliser ce schéma pour indiquer également des exemples de requêtes. 
- ajouter quelques notions dans le plan qui pourront ensuite servir pour le développement (pour gagner du temps); 
  par exemple
    - "tête" d'une requête calcul (pour le développement du théorème de Codd)
    - homomorphisme entre deux requête calculs (?) (pour développement de la preuve inclusion est NP complet) 
- parler du renommage des tables après la jointure (motivation: exemple d'autojointure)

## Développements

Remarques générales:
- attention à l'utilisation du tableau (espaces disponible, organisation)
- bien présenter / définir ce qu'on veut monter au début
- rappeler le prérequis déjà acquis (voir plan de la leçon)


### Développement 1: Théorème de Codd

- définir le théorèle et bien expliquer pourquoi il est important (le jury n'est pas forcément composé d'experts en BD...)
- bien expliquer le principe de la preuve au début (preuve inductive en partant des tables comme expressions simples)
- bien choisr les opérateurs (algèbre) ou sous-expressions (calcul) pour lesquels on montre la traduction dans l'autre langage

### Développement 2: NP complétude de l'inclusion requêtes conjonctives

- bien formuler le théorème au début
- donner des indications pourquoi ce théorèle est important
- donner le schéma général de la preuve au début : inclusion = existence d'un homomorphisme; traduction du problème de recherche d'un homomorphisme en problème de trois-colorabilité
- possibilité d'illustrer quelques notions sour forme graphique (par exemple, homomorphisme) pour éviter d'écrire trop de texte ?

 