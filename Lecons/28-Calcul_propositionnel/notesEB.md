# 17/11 - 28.Formules du calcul propositionnel : représentation, formes normales, satisfiabilité. Applications [Emmanuel]

Développements :

   1. **Programmation de la transformation Tseitin <- choisi par le jury**
   2. Éléments de preuve du théorème de complétude (propositionnel)

## Développement

### Présentation tableau

Description mathématique de Tseitin: fonction qui transforme une formule phi en une autre formule T(phi) équivalente (au sens de la satisfiabilité) qui sera en CNF et qui contiendra des nouvelles variables

### Présentation de code

Langage choisi : OCaml

Définition d'un module type décrivant les formules:

   * données
   * constructeurs (y compris conjonction)
   * printers
   * evaluate : model -> formula -> bool
   * tseitin\_transform : formula -> string -> formula

Module FormulaTree : Formula

   * formula sous forme d'AST
   * implémentation triviale des fonctions
   * transforme formule pour garder que And et Not
(j'ai plus de batterie :( ) up to you

Description de l'algorithme :

   * À chaque sous-formule (= sous-arbre) psi de notre formule phi de base, on associe une formule atomique c\_psi, représenté par un entier.
   * Pour ce faire, on procède récursivement pour chaque sous-formule en renvoyant le prochain indice disponible pour nommer les nouvelle formules atomiques.

## Questions (et remarques) du jury

### Sur le développement

   * précisions demandées sur le type des variables utilisées dans la définition mathématique
   * Détailler la transformation sur un exemple (pendant que Yaëlle gère le projo) -> en fait non, on passe au code directement.
   * Type de retour dans le programme : la fonction renvoie un triplet : à quoi les valeurs correspondent-elles ?
       * 1er membre ???
       * 2e membre liste des équivalences
       * 3eme membre nombre de variables qui ont été introduit
       * Emmanuel se rend compte d'un bug dans le programme -> en fait c'est bon -> en fait non ?. En tous cas il hésite. Le jury l'aide à déboguer, Emmanuel modifie le code en live (quel courage)
   * "équivalent a" d'où  vient le "a" ?
       * C'est le mot-clé qui signifie "<->". Le jury suggère d'utiliser directement le symbole "<->".
   * Aurais-tu pu éviter ton erreur ?
       * Oui, en renvoyant une chaîne de caractère plutôt
           * Plus globalement, se servir du système de type
   * Utiliser la syntaxe "let a, b, c = triplet in" plutôt que "match triplet with a, b, c ->"
   * Le jury soutient que le programme ne respecte pas la spec annoncée au tableau : application de la formule au tableau sur l'exemple déjà traité
   * Problème de l'absence de cas de base dans le formulation
       * En fait la spec n'était pas bonne : le jury et Emmanuel détaillent.
   * Gestion des nom de variable fraîche : on aurait pu implémenter ça dans une autre fonction pour éviter que ça pollue le code (book keeping qui n'aide pas à la compréhension). D'un autre côté, ça permet d'expliciter des aspects de complexité.
   * Peut tu rappeler la table de vérité du xor ? Emmannuel a présenté l'équivalence (càd NXOR) et non le xor dans l'exemple.
   * Intérêt de la CNF ? -> Plus simple à satisfaire
   * Pourquoi Tseitin ? en fait la transformation en CNF est exponentielle dans le cas général, alors que Tseitin donne une 3-CNF linéaire -> permet de réduire SAT en 3-SAT
   * 2-SAT est P-Complet : comment on prouve la P-Difficulté ?
       * En fait c'est NL-Complet (donc c'est NL, or on ne sait pas si NL est strictement inclus dans P)
   * Remarque pour OCaml : on peut créer un nouveau type "type cnf = formula" et on annote les fonctions.

### Sur le plan

   * Equivalence logique entre les deux formules (¬¬A <-> A) et ((¬¬¬A \&\& ¬A) || (¬¬A \&\& A)). En remplaçant (¬A) par (A) et (A) par (B), on obtient (A <-> B) à gauche et ((¬A \&\& ¬B) || (A \&\& B)) à droite.
   * Remarque : motiver ce dont on parle dans le plan. Ce qui intéresse le jury, c'est ce qui n'est **pas** marqué dans le plan (par exemple : intérêt de tel définition, de tel théorème ou de tel exemple). Par exemple l'intérêt de de s'intéresser au problème SAT qui prend une CNF en entrée donc on a besoin de savoir ce que c'est qu'une CNF et de l'algorithme de Tseitin pour avoir une reformulation non exponentielle d'une formule . <- Genre de chose qu'on attend.
   * Différence en théorème de correction et théorème de complétude (pas différencié dans le plan d'Emmanuel).
           * Correction : Sens T |- phi implique T |= phi (sens facile) -> trop light pour un développement.
           * Complétude : Sens T |= phi implique T |- phi (sens plus dur et plus intéressant)
   * Calcul des séquents : intérêt ? À quoi correspond la coupure en calcul des séquents ?
           * On s'éloigne de la déduction naturelle (façon naturelle de raisonner), mais plus facile à automatiser (la recherche de preuve dans le calcul des séquents termine si on a pas la coupure).
   * motivation : à quoi servent les formes normales minimales ?
           * circuit reconfigurable, avoir les plus petits circuits possibles
   * différence CNF / DNF : algo linéaire pour CNF. Est ce qu'on peut trouver efficacement une DNF ?
           * Satisfaire un DNF se fait en temps polynomial, une telle réduction montrerait P = NP.
   * Mettre un peu plus en valeur l'algo dans le plan et préparer plus des questions autour de ça. Pourquoi est ce que le problème SAT est intéressant?
           * Réduction à SAT pour prouver la NP-Difficulté d'un pb
           * Il existe des solveurs SAT qui marchent plutôt bien en pratique, on peut réduire un problème dur en une version SAT et le donner à un solveur.
   * Manque d'exemples, de liant, de motivations -> c'est à ça que sert la présentation du plan.
