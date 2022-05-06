from typing import List, Callable

def next_fit (objects: List[int], c: int, pp = False) -> int:
    ''' Next Fit
    on ajoute toujours au dernier conteneur,
    et on ajoute un nouveau quand on ne peut pas
    '''
    if len(objects) == 0:
        return 0
    bins : List[int] = [[]]
    # pour chaque objet
    for o in objects:
        # si on a de la place, on ajoute
        if sum(bins[-1]) + o <= c:
            bins[-1].append(o)
        # sinon on rajoute un conteneur a la fin
        else:
            bins.append([o])
    if pp:
        for b in bins:
            print(b)
    # le nombre de conteneurs a la fin
    return len(bins)

def fit_first (objects: List[int], c: int, pp = False) -> int:
    ''' Fit First
    on ajoute au premier conteneur qui a de la place,
    et on ajoute un nouveau s'il n'y en a pas
    '''
    if len(objects) == 0:
        return 0
    bins : List[int] = [[]]
    # pour chaque objet
    for o in objects:
        bin_idx : int = -1
        # on cherche un conteneur qui a de la place
        for cnt in range(len(bins)):
            if sum(bins[cnt]) + o <= c:
                bin_idx = cnt
                break
        # s'il y en a un, on y ajoute l'objet
        if bin_idx >= 0:
            bins[bin_idx].append(o)
        # sinon on rajoute un conteneur a la fin
        else:
            bins.append([o])
    if pp:
        for b in bins:
            print(b)
    # le nombre de conteneurs a la fin
    return len(bins)

def best_fit (objects: List[int], c: int, pp = False) -> int:
    ''' Best Fit
    on ajoute au conteneur qui a le moins de place,
    et on ajoute un nouveau s'il n'y en a pas
    '''
    if len(objects) == 0:
        return 0
    bins : List[int] = [[]]
    # pour chaque objet
    for o in objects:
        bin_idx : int = -1
        bin_room : int = c+1
        # on cherche le conteneur qui a le moins de place
        for cnt in range(len(bins)):
            room : int = c - sum(bins[cnt])
            if room >= o and room < bin_room:
                bin_idx = cnt
                bin_room = room
        # s'il y en a un, on y ajoute l'objet
        if bin_idx >= 0:
            bins[bin_idx].append(o)
        # sinon on rajoute un conteneur a la fin
        else:
            bins.append([o])
    if pp:
        for b in bins:
            print(b)
    # le nombre de conteneurs a la fin
    return len(bins)

def best_fit_decreasing (objects: List[int], c: int, pp = False) -> int:
    ''' Best Fit Decreasing
    best fit, mais en triant préalablement les objets par poids décroissant
    '''
    return best_fit(sorted(objects, reverse=True), c, pp)

def fit_first_decreasing (objects: List[int], c: int, pp = False) -> int:
    return fit_first(sorted(objects, reverse=True), c, pp)

def waste(strat: Callable[[List[int], int], int], objects: List[int], c: int) -> int:
    ''' waste(strat, c, objects) -> c*||strat|| - sum(objects)
    ie l'espace vide quand on applique strat à (objects ; c)
    '''
    return c*strat(objects, c) - sum(objects)
