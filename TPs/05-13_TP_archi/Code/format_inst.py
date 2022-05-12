from enum import Enum, auto
from bitArray import BitArray


class InstructionInconue(Exception):
    """ Execption levé lors d'un opcode inconu """

    def __init__(self, opcode, *args):
        super().__init__(args)
        self.opcode = opcode

    def __str__(self):
        return f'{self.opcode} n\'est pas un opcode valide'

class Format(Enum):
    R  = 0
    I  = 1
    S  = 2
    SB = 3
    U  = 4
    UJ = 5
    X  = -1

    def fmt(inst):
        inst_fmt = Format.X
        try :
            inst_fmt = list_format[Format.opcode(inst)]
        except KeyError as ex:
            pass
        finally:
            if inst_fmt == Format.X:
                raise InstructionInconue(Format.opcode(inst))
            return inst_fmt

    def opcode(inst):
        return inst[0:7]

    def rd(inst):
        return inst[7:12]

    def rs1(inst):
        return inst[15:20]

    def rs2(inst):
        return inst[20:25]

    def funct3(inst):
        return inst[12:15]

    def funct7(inst):
        return inst[25:32]

    def imm(inst):
        inst_fmt = Format.fmt(inst)
        if (inst_fmt == Format.I):
            return inst[20:32]
        elif (inst_fmt == Format.S):
            return inst[7:12]+inst[25:32]
        elif (inst_fmt == Format.SB):
            return inst[8:12] + inst[25:31] + inst[7:8] + inst[31:32]
        elif (inst_fmt == Format.U):
            return inst[12:32]
        elif (inst_fmt == Format.UJ):
            return inst[21:31]+inst[20:21]+inst[12:20]+inst[31:32]
        raise ValueError("Format d'instruction invalide")

list_format = {
    BitArray(b'1100110') : Format.R,
    BitArray(b'1100100') : Format.I,
    BitArray(b'1100000') : Format.I,
    BitArray(b'1110011') : Format.I,
    BitArray(b'1100111') : Format.I,
    BitArray(b'1100010') : Format.S,
    BitArray(b'1100011') : Format.SB,
    BitArray(b'1111011') : Format.UJ,
    BitArray(b'1110110') : Format.U,
    BitArray(b'1110100') : Format.U
}
