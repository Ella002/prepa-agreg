from bitArray import BitArray

class Registre:
    """
    Crée un registre de taille bits

    Pour créer un registre 32 bits:
    >>> reg = Registre(32)

    Pour écrire une valeur (doit être de type BitArray)
    >>> bval = BitArray(32)
    >>> bval.from_uint32(255)
    >>> reg.ecriture(bval)
    >>> print(reg.lecture())
    00000000 00000000 00000000 11111111

    >>> bval = BitArray(5)
    >>> bval.from_uint32(23)
    >>> reg[10:15] = bval
    >>> print(reg.lecture())
    00000000 00000000 01011100 11111111
    """
    def __init__(self, taille):
        self.bits = BitArray(taille=taille)

    def __getitem__(self, indice):
        return self.bits[indice]

    def __setitem__(self, indice, val):
        if isinstance(indice, slice) and not isinstance(val, BitArray):
            raise TypeError("la valeur doit être de type BitArray")

        if isinstance(indice, int) and not isinstance(val, bool):
            raise TypeError("la valeur doit être de type Bool")

        self.bits[indice] = val

    def __copy__(self):
        return self.bits

    def __str__(self):
        return str(self.bits)

    def __len__(self):
        """
        retourne la taille du registre en bits
        """
        return len(self.bits)

    def ecriture(self, val):
        if type(val) is not BitArray or len(val) != len(self):
            raise TypeError("la valeur doit être de type BitArray[{}]".format(len(self)))

        self.bits[:] = val[:]

    def lecture(self):
        return self.bits
