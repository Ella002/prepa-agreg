# Jules #



## Commentaires ##



RqDYaëlle: attention, dans l'algo au tableau tu as renommé tes variables en plein milieu (base est devenu B)



RqDChatain: tu as dit beaucoup beaucoup de choses, traité (presque) tout le sujet... Visiblement tu as bien compris le sujet

Attention par contre que tu passes très vite sur tout, tu es obligé de foncer. Du coup on perd de l'aspect pédagogique, et les preuves de certains résultats

Pas d'exemples :(

Il manque un exemple pour les représentations, un dessin pour les circuits...

Si l'addition en chiffres signés est détaillée, le reste devient plus facultatif

Réponse de Jules: j'avais peur qu'il y ait pas assez d'apport personnel si je me cantonnais à l'addition

Réponse de T. Chatain: non, là l'apport personnel c'est plus de détailler les preuves qui ne sont pas dans le sujet, d'explorer les recoins que le sujet ne fait qu'aborder



RqDChatain: c'est bien de mettre les *titres* de chaque partie, pas juste les numéros



RqDChatain: bonne utilisation du tableau, juste pas assez de détails dans le discours



En règle générale pour ce type de sujet, il y a un joli résultat (ici, que l'addition en chiffres signés est de profondeur 1), dont la preuve est à détailler

Par contre, prendre le temps d'expliquer les résultats plus simples. Par exemple, l'existence et l'unicité de la représentation en complément pour les chiffres dans tel intervalle. Et le domaine des chiffres représentables en chiffres signés, résultat qui mérite une preuve.

RqDChatain: ce que t'as implémenté c'est bien, mais il y en a peut-être un peu trop. Il ne faut pas y passer trop de temps, surtout en préparation.

Rq: pour les exercices, on peut tout à fait effacer des trucs, il faut juste demander quoi


## Questions ##



Q: comment tu expliques le domaine de valeurs de β

R: on ne peut pas avoir de chiffres plus grand que la base

[prend un stylo pour expliquer]

β est suffisamment grand pour représenter un intervalle d'entiers, sans trous

RqDChatain: écrire les petits exemples (éventuellement faire référence aux gros si y a pas de place, mais ce n'est pas le cas ici)



Q: quand on utilise la représentation en chiffres signés, on perd l'unicité de la représentation, mais ça rajoute de la flexibilité qui permet d'améliorer la complexité du calcul de l'addition.

R: oui, on assure que la retenue ne se propagera pas trop

Rq: le fait de mettre une flexibilité pour diminuer la complexité est un phénomène répandu, par exemple avec les a-b arbres (arbres où on peut avoir entre a et b fils)



Rq: ça vaudrait le coup de refaire à la maison les preuves



Q: qu'en est-il de l'égalité de ces entiers?

R: déjà, le 0 est représenté de manière unique. Pour savoir si deux nombres sont égaux, il suffit de soustraire l'un à l'autre, et vérifier si le résultat est 0.



Q: Quel est l'intervalle des entiers représentables en chiffres signés?

R: Pour n bits, on va de |[ -β (B^n - 1)/(B - 1) ; β (B^n - 1)/(B - 1) ]|

Du coup, avec n chiffres, on peut représenter:

* en rep signée: 2 * β * (B^n - 1)/(B - 1) + 1

* en rep complément: B^n

Q: si on a k bits, combien va-t-on représenter de nombres dans un cas et dans l'autre?

R:

* Rep complément: un chiffre dans l'intervalle |[0 ; B-1]| nécessite log<sub>2</sub>(B) bits

	k bits -> k/log<sub>2</sub>(B) chiffre, B^(k/log<sub>2</sub>(B))

* Rep chiffr signé: un chiffre dans l'intervalle |[ -β ; β ]| nécessite log<sub>2</sub>(2β+1)

    k bits -> k/log<sub>2</sub>(2β+1) chiffres, 2 β B^(k/log<sub>2</sub>(2β+1)) [RqDY: j'ai rien compris]

RqDChatain: il se peut que le jury pose une question un peu compliquée comme ça, qui en plus ne sert pas à grand chose et pendant laquelle le jury s'endort => faire toujours des réponses courtes, et si le jury pose une question qui mérite un développement long, présenter le plan de la preuve et laisser le jury choisir ce qu'on développe. Ça évite de perdre du temps sur des questions pas très utiles, au lieu de prouver comment on est fort
