class BitArray:
    """BitArray permet de définir des vecteurs de bits de taille fixe
    encodé sous forme de liste de booleens.

    Chaque bit peux valoir True, False ou None si aucune valeur n'a
    été définie pour ce bit.

    Déclaration d'un vecteur de 8 bits non initialisé:
    >>> bvec = BitArray(taille=8)
    Chaque bit est accessible individulement:
    >>> bvec[1]
    None
    >>> bvec[1]=False
    >>> bvec[1]
    False

    Ou part slice:
    >>> bvec[2:5]
    [None, None, None]
    >>> bvec[2:5] = [True, False, True]
    >>> bvec[2:5]
    [True, False, True]

    >>> bvec.from_unit8(170)
    >>> bvec
    b'01010101'
    >>> bvec.to_uint()
    170
    """

    def __init__(self, val=None, taille=0):
        if isinstance(val, list):
            # On vérify si c'est bien une liste de booléen
            for i in val:
                if i is not None and not isinstance(i, bool):
                    raise ValueError("val doit être une liste de booléen:\n{}".format(val))
            self.taille = len(val)
            self.bits = val

        elif isinstance(val, bytes):
            self.taille = len(val) if taille == 0 else taille
            self.bits = [None] * self.taille
            self.from_bytes(val)

        elif taille < 1:
            raise ValueError(f"La taille du vecteur de bits doit être supérieur ou égale à 1 pour le type {type(val)}")

        else:
            self.bits = [None] * taille
            self.taille = taille

            if isinstance(val, int):
                self.from_int(val)
            elif val is not None:
                raise TypeError(f"Le type de valeur ne peut être {type(val)}")

    def __getitem__(self, indice):
        if isinstance(indice, slice):
            start, stop, step = indice.start, indice.stop, indice.step
            if start is not None and (start < 0 or start >= self.taille):
                raise IndexError("Indice de début non valide")
            if stop is not None and (stop < start or stop > self.taille):
                raise IndexError("Indice de fin non valide")

            return BitArray(self.bits[indice])
        else:
            return self.bits[indice]

    def __setitem__(self, indice, val):
        if isinstance(indice, slice):
            start, stop, step = indice.indices(self.taille)
            if start not in range(0, self.taille):
                raise IndexError("indice non valide")

            for i in range(start, stop, step):
                self.bits[i] = val[i-start]
        else:
            if indice not in range(0, self.taille):
                raise IndexError("indice non valide")
            self.bits[indice] = val


    def boolstr(self, x):
        return 'X' if x == None else '1' if x else '0'

    def __repr__(self):
        return "BitArray("+ repr(self.bits) + ")"

    def __str__(self):
        val = "".join(map(self.boolstr, self.bits))
        return " ".join(val[i:i+8] for i in range(0, self.taille, 8))[::-1]

    def __hash__(self):
        return self.to_int()

    def __len__(self):
        """ Permet d'obtenir la taille d'un mot binaire avec la fonction len()
        >>> len(BitArray(b'000'))
        3
        """
        return self.taille

    def __eq__(self, other):
        if not isinstance(other, BitArray):
            raise TypeError(f'BitArray ne peut pas être comparé avec {type(other)}')

        return self.bits == other.bits

    def __add__(self, other):
        """ Permet la concatenation de mots binaires:
        >>> m = BitArray(7,4)
        >>> n = BitArray(5,4)
        >>> n+m
        BitArray([True, False, True, False, True, True, True, False])
        """
        if not isinstance(other, BitArray):
            raise TypeError(f'BitArray ne peut pas être ajouté avec {type(other)}')
        return BitArray(self.bits + other.bits)

    def from_int(self, valeur, taille=0, unsign=False):
        if taille == 0:
            taille=self.taille

        bitsext, bitsval = (0, self.taille) if self.taille < taille else (self.taille - taille, taille)

        for i in range(0, bitsval):
            self.bits[i] = (valeur % 2) == 1
            valeur = valeur >> 1

        if bitsext > 0:
            for i in range(bitsval, bitsval+bitsext):
                self.bits[i] = False if unsign else self.bits[bitsval-1]

    def from_int32(self, valeur):
        """ from_unit32() convertie un entier 32bits signé.
        """
        self.from_int(32, valeur)

    def from_int16(self, valeur):
        """ from_unit16() convertie un entier 16bits signé.
        """
        self.from_int(16, valeur)

    def from_int8(self, valeur):
        """ from_nit8() convertie un entier 8bits signé.
        """
        self.from_int(8, valeur)

    def from_uint32(self, valeur):
        """ from_unit32() convertie un entier 32bits non signé.
            La valeur entière est tronquée si besoin
        """
        self.from_int(32, valeur, unsign=True)

    def from_uint16(self, valeur):
        """ from_unit16() convertie un entier 16bits non signé.
            La valeur entière est tronquée si besoin
        """
        self.from_int(16, valeur, unsign=True)

    def from_uint8(self, valeur):
        """ from_unit8() convertie un entier 8 bits non signé.
            La valeur entière est tronquée si besoin
        """
        self.from_int(8, valeur, unsign=True)

    def to_int(self, unsign=False):
        """ to_int() convertie la valeur signée du bitArray en integer.
            Le paramettre unsign permet de forcé un convertion non signée (unsign=True)
        """
        val = 0

        for i in range(0, self.taille-1):
            val = val + self[i]*2**i

        val = (1 if unsign else -1) * self[self.taille-1]*2**(self.taille-1)+val

        return val

    def to_uint(self):
        """ to_uint() convertie la valeur du bitArray en integer non signé.
        """
        return self.to_int(unsign=True)

    def from_bytes(self, valeur, unsign=False):
        """ from_bytes() convertie valeur de type bytes en bitArray
            la conversion se fait en non signé
            valeur est tronqué à la taille du bitArray
        """
        for i in range(0, len(valeur)):
            if chr(valeur[i]) == '1':
                self[i] = True
            elif chr(valeur[i]) == '0':
                self[i] = False
            elif chr(valeur[i]) == 'X':
                self[i] = None
            else:
                raise ValueError("from_bytes(): valeur n'est pas une chaine binaire")

        for i in range(len(valeur), self.taille):
            self[i] = False if unsign else self.bits[len(valeur)-1]

    def to_bytes(self):
        """ to_bytes() renvoie la valeur du bitArray sous form de bytes
        """
        return bytes("".join(map(self.boolstr, self.bits)), 'ascii')
