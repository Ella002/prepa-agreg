from registre import Registre
from bitArray import BitArray

class BancRegistre:
    """
    Crée un Banc de nb registre de largeur taille

    Création d'un banc de 4 registres de 16bits.
    Le registre R[0] est collé à 0
    >>> R = BancRegistre(4, 16)
    R0: 00000000 00000000
    R1: XXXXXXXX XXXXXXXX
    R2: XXXXXXXX XXXXXXXX
    R3: XXXXXXXX XXXXXXXX

    R1, R2 et R3 n'ont pas été initialisé

    >>> bval = BitArray(16)
    >>> bval.from_int16(1)
    >>> R[1] = bval
    >>> bval.from_int16(2)
    >>> R.ecriture(2, bval)
    >>> print(R)
    R0: 00000000 00000000
    R1: 00000000 00000001
    R2: 00000000 00000010
    R3: XXXXXXXX XXXXXXXX

    >>> R[1]
    b'1000000000000000'
    >>> type(R[1])
    <class 'bitArray.BitArray'>

    >>> print(R[1])
    00000000 00000001

    >>> R[3] = R[1]
    >>> print(R)
    R0: 00000000 00000000
    R1: 00000000 00000001
    R2: 00000000 00000010
    R3: 00000000 00000001

    """

    def __init__(self, nb, taille):
        if nb < 1:
            raise ValueError("nb doit être au moins égale à 1")

        self.banc = [Registre(taille)]
        for i in range(1, nb):
            self.banc.append(Registre(taille))

        self.nb = nb
        self.taille = taille
        self.banc[0].ecriture(BitArray(0, self.taille))

    def __getitem__(self, indice):
            return self.banc[indice].lecture()

    def __setitem__(self, indice, val):
        if type(val) is not BitArray:
            raise TypeError("la valeur doit être de type BitArray")
        if indice == 0:
            return

        self.banc[indice].ecriture(val)


    def __str__(self):
        val=""
        for i in range(0, len(self)):
            val += "R{}: {}\n".format(i, self[i])

        return val

    def __len__(self):
        return self.nb

    def lecture(self, num):
        return self.banc[num].lecture()

    def ecriture(self, num, val):
        self[num] = val
