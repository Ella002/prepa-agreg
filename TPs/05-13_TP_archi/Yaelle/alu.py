import traceback
from bitArray import BitArray

from typing import Tuple

class OperationInvalide(Exception):
    """ Execption levé lors d'un opcode inconu """

    def __init__(self, opcode, *args):
        super().__init__(args)
        self.opcode = opcode

    def __str__(self):
        return f'{self.opcode} n\'est pas un opcode valide'

class Alu:
    def __init__(self):
        self.carry = False
        self.overflow = False
        self.sign = False

    def __str__(self):
        return f"""
op:  {self.op}
x:   {self.x}
y:   {self.y}
res: {self.res}
carry: {self.carry}\t overflow: {self.overflow}\t zero: {self.zero}\t sign: {self.sign}
        """

    def set_zero_flag(self):
        self.zero = False

        for i in range(len(self.x)):
            self.zero |= self.res[i]

        self.zero     = not self.zero

    def set_sign_flag(self):
        self.sign     = self.res[-1]

    def add(self, cin=False):
        ''' add(self, False) calcule self.x + self.y,
        et met à jour self.res, self.carry et self.overflow
            add(self, True) calcule self.x + self.y + 1,
        et met à jour self.res, self.carry et self.overflow
        '''
        # Additionneur n bits (mode=False)
        # soustracteur si mode=True
        # on vérifie que les deux opérandes ont la même longueur
        assert (len(self.x) == len(self.y))

        def add1bit (a: bool, b: bool, cin: bool) -> Tuple[bool, bool]:
            ''' add1bit(a, b, cin) renvoie le resultat et la carry
            de l'addition sur un bit: a+b+cin
            '''
            s : bool = a ^ b ^ cin
            cout : bool = a & b | a & cin | b & cin
            return s, cout

        nbbits = len(self.x)
        # si sub, on fait a + b + 1, dc carry = True
        carry = cin
        self.res = BitArray(0, nbbits)
        for i in range(nbbits):
            s, carry = add1bit(self.x[i], self.y[i], carry)
            self.res[i] = s

        self.carry = carry

        # overflow flag = 1 si les deux operandes sont du meme signe,
        # et le resultat d'un signe different
        self.overflow = self.x[-1] == self.y[-1] and self.x[-1] != self.res[-1]


    def sub(self):
        ''' sub(self) calcule self.x - self.y
        et met à jour self.res, self.carry et self.overflow
        '''
        def neg(ba: BitArray) -> BitArray:
            ''' neg(ba) renvoie la negation de ba'''
            return BitArray([not b for b in ba.bits])
        # on inverse y
        self.y = neg(self.y)
        # on appelle l'additionneur, avec la carry initial a 1
        self.add(cin = True)
        # on inverse la carry
        self.carry = not self.carry

    def sll(self):
        ''' sll(self) calcule self.x << self.y
        et met à jour self.res
        NB: pas de maj des flags
        '''
        nbbits = len(self.x)
        # on convertit self.y en entier pour connaitre le decalage
        dec = self.y.to_uint()
        # on ajoute autant de 0 du cote faible du bitarray
        bits_dec = [False]*dec + self.x.bits
        # on garde les nbbits de poids faible
        self.res = BitArray(bits_dec[0:nbbits])


    def sr(self, arith=False):
        ''' sr(self, False) calcule self.x >>l self.y, ie on ajoute des 0,
            sr(self, True) calcule self.x >>a self.y, ie on ajoute le bit de signe,
        et met a jour self.res
        '''
        nbbits = len(self.x)
        # on convertit self.y en entier pour connaitre le decalage
        dec = self.y.to_uint()
        # bit a ajouter: soit 0, soit le bit de signe
        bit = self.x[-1] if arith else False
        # on ajoute ce bit du cote fort du bitarray
        bits_dec = self.x.bits + [bit]*dec
        # on garde les nbbits de poids fort
        self.res = BitArray(bits_dec[dec:nbbits+dec])

    def xor(self):
        ''' xor(self) calcule self.x ^ self.y, bit à bit
        et met à jour self.res
        NB: pas de maj des flags
        '''
        assert (len(self.x) == len(self.y))

        nbbits = len(self.x)
        self.res = BitArray(taille=nbbits)
        for i in range(nbbits):
            self.res[i] = self.x[i] ^ self.y[i]

    def bor(self): # or
        ''' or(self) calcule self.x | self.y, bit à bit
        et met à jour self.res
        NB: pas de maj des flags
        '''
        assert(len(self.x) == len(self.y))

        nbbits = len(self.x)
        self.res = BitArray(taille=nbbits)
        for i in range(nbbits):
            self.res[i] = self.x[i] | self.y[i]

    def band(self): # and
        ''' and(self) calcule self.x & self.y, bit à bit
        et met à jour self.res
        NB: pas de maj des flags
        '''
        assert (len(self.x) == len(self.y))

        nbbits = len(self.x)
        self.res = BitArray(taille=nbbits)
        for i in range(nbbits):
            self.res[i] = self.x[i] & self.y[i]

    def eval(self, alu_op, x, y):
        self.op = alu_op
        self.x = x
        self.y = y
        self.res = BitArray(0, len(x))

        self.carry    = False
        self.overflow = False

        try:
            if self.op.to_bytes() == b'0000': # add
                self.add()
            elif self.op.to_bytes() == b'1000': # sub
                self.sub()
            elif self.op.to_bytes() == b'0100': # sll
                self.sll()
            elif self.op.to_bytes() in [b'0101', b'1101']: # srl et sra
                self.sr(arith=self.op[0])
            elif self.op.to_bytes() == b'0011': # or
                self.bor()
            elif self.op.to_bytes() == b'0111': # and
                self.band()
            elif self.op.to_bytes() == b'0001': # xor
                self.xor()
            else:
                print(f"ALU Operation {self.op.to_bytes()}")
                raise OperationInvalide(self.op)
        except TypeError as e:
            traceback.print_exc()
            print(f"op: {self.op}")
            print(f"X: {self.x}")
            print(f"Y: {self.y}")
            raise e

        self.set_sign_flag()
        self.set_zero_flag()
