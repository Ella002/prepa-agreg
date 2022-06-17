import typing as typ

class Transition(typ.NamedTuple):
    longueur: int
    duree: int
    suivant: int


class Chemin(typ.NamedTuple):
    longueur: int
    duree: int
    trajet: list[int]


def plus_long_chemin(
        graphe: list[list[Transition]],
        depart: int,
        limite: int,
        bavard: bool,
        est_considere: typ.Callable[[int], bool]
        ) -> Chemin:
    """Renvoie le plus long chemin effectuable depuis depart en temps limite.
    """
    if bavard:
        msg = "Recherche du plus long chemin effectuable en {} secondes (i.e. effectuable {} fois par seconde)"
        print(msg.format(limite, 1 / limite))

    meilleur = Chemin(longueur=0, duree=0, trajet=[depart])
    chemins: list[Chemin] = [meilleur]

    while chemins != []:
        chemin = chemins.pop()
        sommet = chemin.trajet[-1]

        if not(est_considere(sommet) or sommet in range(len(graphe))):
            continue

        for transition in graphe[sommet]:
            if (transition.duree + chemin.duree > limite):
                continue

            nouveau_chemin = Chemin(
                    longueur = chemin.longueur + transition.longueur,
                    duree    = chemin.duree    + transition.duree,
                    trajet   = chemin.trajet   + [transition.suivant]
            )

            if nouveau_chemin.longueur > meilleur.longueur:
                meilleur = nouveau_chemin

            chemins.append(nouveau_chemin)

    if meilleur.duree <= meilleur.longueur:
        if meilleur.duree != 0:
            vitesse = meilleur.longueur / meilleur.duree
        if bavard:
            print("vitesse moyenne : {}s".format(vitesse))

    return meilleur


g = [
        [
            Transition(longueur=2, duree=1, suivant=1),
            Transition(longueur=3, duree=2, suivant=2),
        ], [
            Transition(longueur=5, duree=3, suivant=3),
        ], [
            Transition(longueur=0, duree=0, suivant=1),
            Transition(longueur=0, duree=1, suivant=3),
        ], [
    ]
]

yes = lambda x: True
no = lambda x: False

g_faux = [[Transition(longueur=0, duree=0, suivant=1)]]

def est_dans_bornes(g: list[list[Transition]]) -> typ.Callable[[int], bool]:
    return (lambda x: x in range(len(g)))

def test1():
    print("# Test 1")

    res = plus_long_chemin(g, depart=0, limite=5, bavard=False,
            est_considere=yes)
    assert res == Chemin(longueur=8, duree=5, trajet=[0, 2, 1, 3])

    res = plus_long_chemin(g, depart=2, limite=0, bavard=False,
            est_considere=yes)
    assert res == Chemin(longueur=0, duree=0, trajet=[2])

    res = plus_long_chemin(g_faux, depart=0, limite=100, bavard=False,
            est_considere=est_dans_bornes(g_faux))
    assert res == Chemin(longueur=0, duree=0, trajet=[0])

    print("=> Pas d'erreur dans le test 1")


def test2():
    print("# Test 2 : Passer par tous les chemins")

    res = plus_long_chemin(g, depart=0, limite=5, bavard=True,
            est_considere=yes)
    assert res == Chemin(longueur=8, duree=5, trajet=[0, 2, 1, 3])

    res = plus_long_chemin(g, depart=2, limite=0, bavard=True,
            est_considere=yes)
    assert res == Chemin(longueur=0, duree=0, trajet=[2])

    print("=> Pas d'erreur dans le test 2")


def test3():
    print("# Test 3 : Passer par toutes les arêtes")
    res = plus_long_chemin(g, depart=2, limite=1, bavard=True,
            est_considere=yes)
    assert res == Chemin(longueur=0, duree=0, trajet=[0])
    print("=> Pas d'erreur dans le test 3")


def test41():
    print("# Test 4.1 : Conditions multiples")
    res = plus_long_chemin(g_faux, depart=0, limite=10, bavard=True,
            est_considere=yes)
    assert res == Chemin(longueur=0, duree=0, trajet=[0])
    print("=> Pas d'erreur dans le test 4.1")


def test42():
    print("# Test 4.2 : Conditions multiples")
    res = plus_long_chemin(g, depart=0, limite=5, bavard=False,
            est_considere=no)
    assert res == Chemin(longueur=0, duree=0, trajet=[0])
    print("=> Pas d'erreur dans le test 4.2")
