import traceback
from bitArray import BitArray

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

    def add(self, mode=False):
        # Additionneur n bits (mode=False)
        # soustracteur si mode=True
        raise NotImplemented

    def sub(self):
        raise NotImplemented

    def sll(self):
        raise NotImplemented


    def srl(self, arith=False):
        raise NotImplemented

    def xor(self):
        raise NotImplemented

    def bor(self): # or
        raise NotImplemented

    def band(self): # and
        raise NotImplemented

    def eval(self, alu_op, x, y):
        self.op = alu_op
        self.x = x
        self.y = y
        self.res = BitArray(0, len(x))

        self.carry    = False
        self.overflow = False

        try:
            if self.op.to_bytes() in [b'0000', b'1000']: # add
                self.add(mode=self.op[0])
            elif self.op.to_bytes() == b'0100': # sll
                self.sll()
            elif self.op.to_bytes() in [b'0101', b'1101']: # srl
                self.srl(arith=self.op[0])
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
