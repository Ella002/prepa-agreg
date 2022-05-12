# Yaëlle #



## Plan ##



   1. Définitions et notations
   1. Aspects algorithmiques
       1. Next Fit ⏭️
       1. Fit First 🥇
       1. Best Fit 🌟
       1. Comparaisons stratégies ⚖️


## Questions ##

❔ NP-complet nécessite problème de décision, or ici c'est un problème d'optimisation. De quel problème d'optimisation parles-tu ?

➡️ Plutôt que "Trouver le rangement qui minimise le nombre de boîte", "Peut-on ranger tous les x avec k boîtes ?"



❔ Preuve de la borne de fit first: n\_boites\_fit\_first <= ceil(2 * n\_boites\_opti / capacité)

➡️ Intuition : les conteneurs sont remplis au moins à la moitié.

Par l'absurde, (* détails de la preuve supprimés car pas intéressants en vrai)



❔ Pourquoi ne pas mesurer par rapport à l'optimal ?

➡️ Trop long à calculer, d'où la notion de perte.



❔ Que peut-on dire si la perte est inférieure strictement à la capacité.

➡️ Le rangement est optimal : mêmes si on déplaçait le plus d'éléments possibles du dernier conteneur dans les autres conteneurs on ne pourrait pas le vider entièrement



❔ Exemple de problème plus dur que NP-complet (ie pas NP) ?

➡️ Rush hour par exemple.



❔ Si le problème devient Tetris (objets avec forme), est-ce que ça reste NP-complet ?

➡️ Pour la étant donnée une solution, la vérification se fait en temps poly



❔ Structure de donnée pour l'ensemble des conteneurs ? Complexité associée ?

➡️ ABR. Mieux : arbre rouge-noir, arbre splay, b-arbres



## Remarques ##

📝 Très bonne présentation (jury unanime)

📝 Manque des preuves (cf questions). Une preuve simple d'un "résultat mathématique croustillant" suffit !
