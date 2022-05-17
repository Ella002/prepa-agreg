# 5/05 - 21. Échanges de données et routage. Exemples. - Renaud #

Développements :

- protocole http avec programmation d'un mini serveur Web [RDY: ça me rappelle mon dev de prog web, ça :D]

- **OSPF avec Dijkstra (choisi)**



## Développement: OSPF ##



Routage par états de liens



Decouvrir ses voisins:

    Les routeurs s'envoie des HELLO régulièrement pour que leurs voisins connaissent leur présence

    Le coût entre 2 noeuds : c= 10^8 / (debits:bits par secondes)



Transmission de l'états de lien:

    LSU: -identifiant du routeur emetteur

              -pour chaque voisin l'identifiant du routuer cible et le coût

              -numero de version

              -âge



Une fois tous les messages LSU reçus, chaque routeur calcule les routes les plus courtes vers chaque routeur de la zone -> Dijkstra



<algorithme>



les routeurs stockent l'états de coût de lien





## Questions ##



QSG: OSPF = ?

R: Open Shortest Path First

RqSR: il faut donner les acronymes



RqSR: truc à évoquer à propos des couches



RqSR: vous donnez le découpage en fonction de la taille des réseaux, c'est bien, mais où se trouve Internet?

R: les sources étaient pas d'accord, soit WAN, soit la connexion de tout ça

RSR: Internet c'est la connexion des réseaux locaux



RqSR: systèmes autonomes évoqués plus rapidement à l'oral que dans le plan, mais ça vaut le coup d'en parler



RqSR: vu que vous parlez de DNS, il y a la problématique de traduire adresse IP en nom, mais vous ne mentionnez pas les adresses IP. Il faut en parler.



<discussion sur différence adressage statique / dynamique>



RqEC: le contexte du développement était pas complètement clair



RqEC: rien sur les aspects de sécurité (données non corrompues, identité des personnes), est-ce que c'est hors-sujet?

RSR: c'est une autre approche

R: pour la corruption y a des checksums. OSPF y a des trucs pour identifier, mais pas maîtrisés



QEC: Comment on passe de la découverte des voisins / envoi de HELLO à la transmission de LSU?

R: les HELLO sont envoyés à intervalle régulier. C'est un protocole continu, il ne s'arrête jamais

-> c'était pas clair



RqSR: plutôt que donner l'algo de Dijkstra, éventuellement montrer sur un exemple plutôt, quitte à avoir l'algo sur les notes pour répondre aux questions



QAK: pourquoi OSPF olutôt que rIP?

R: RIP propage très bien les bonne nouvelles, mais en cas de panne ou de lien défaillant l'info va mettre du temps à être propagée.

Plus, RIP compte les sauts, pour OSPF on peut donner un coût aux liaisons (débit).

Plus en OSPF on a des zones, alors que RIP tout le monde parle à tout le monde.



RqSR: c'est difficile avec le stress, mais il faudrait être moins hésitant
