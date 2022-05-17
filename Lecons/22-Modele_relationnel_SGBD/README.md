# 22. Modèle relationnel et conception de bases de données. #

## Version H. Nacke = prof ##

/!\ Attention dans le titre : "conception" c'est PAS la construction d'un SGBD. Conception = dépendances fonctionnelles



### Plan potentiel ###



**Partie 1** : modèle

1/

   * Def Relation
   * Def Tuple, attribut, domaine


2/

   * Def Contraintes
       * contraintes de domaine
       * unicité
       * not null
       * clé
       * clé étrangère
       * Triggers (évoquer/développement possible)


3/

Définir schéma relationnel en SQL:

   * créer table
   * clé primaire
   * clé étrangère
   * contrainte


4/ Exemples



**Partie 2 **: Conception



1/

def : dépendance fonctionnelle + illustrations de situations un peu concrètes des dépendances



2/

Définition de la fermeture à partir d'un attribut : [A]^+\_F : tous les attributs déterminés à partir de A



3/

Algo pour obtenir les clés d'une relation



[...]

--- on pourrait s'arrêter là pour la partie 2 et mettre la partie 2 bis après (modulo alpha-renommage) ---

4/

Définition : décomposition en plusieurs relations



5/

Est-ce que la décomposition est sans perte d'information ?

Algo pour vérifier si la décomposition est SPI (sans perte d'informations)

 - a) cas particulier: décomposition en 2 relations

 - b) cas général : algorithme du tableau (sic)



6/

Décomposition 3FN (Algo de Renaud) (re-sic mais là c'est plus original)



**Partie 2 bis** ? : Modèle entité/Association (surement Partie 3)



1/

Def entité

   * identifiant
   * attribut
   *  réalisme, réification


2/

Définition Association

   * cardinalité: 1-1, 1-n, n-n
   * occurence: 0 ou 1 (aspect optionnel d'une association)
   * arité: binaire, ternaire...


3/

Entité faible



4/

Spécialisation, héritage



5/

Traduction modèle E/A vers un schéma défini à l'aide du modèle relationnel



### Développements possibles ###



- Un des algos de la partie 2 (notamment celui pour avoir les clés les plus petites possibles)

- Trigger (pour les contraintes complexes, partie 1)

- Dév format TP : prendre un fichier html/json pour générer des entrées de table (trop code orienté peut-être)

- Traduction E/A vers relationnel (en général, sur un exemple ?)



### Remarques ###



Ici, la partie 2bis/3 fait une synthèse des deux autres parties, il faut surement ajuster le plan du coup



Mettre des exemples dans le plan



### Questions potentielles ###



- Complexité des algorithmes (au secours, de la théorie) +1
