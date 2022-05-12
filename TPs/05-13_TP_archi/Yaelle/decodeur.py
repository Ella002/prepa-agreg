from bitArray import BitArray
from format_inst import Format
from registre import Registre

class Decodeur:
    """
    Decodeur Intruction RISC-V 32 Bits.

    Decodeur.decode(inst) décode une instruction RISC V 32Bits.
    L'instruction est fournis sous forme de BitArray(32).
    Retourne un tuple contenant les différents champs décodés de l'instruction.
    Retourne le format d'instruction décodée.

    Lève une exception InstructionInconue() si le format de l'instruction n'est pas reconnu
    """
    def calcul_alu_op(self):
        """
        retourne le code opération de l'alu en fonction de l'instruction courante
        """
        opcode = self.opcode.to_bytes()

        if opcode == b'1100110':
            # format R ou I
            funct3 = self.funct3.to_bytes()
            if funct3 == b'010' or funct3 == b'110':
                # slt ou sltu -> sub
                alu_op = BitArray(b'1000')
            else:
                alu_op = BitArray(self.funct7[5], 1) + self.funct3

        elif opcode == b'1100100':
            # format I
            funct3 = self.funct3.to_bytes()
            if funct3 == b'010' or funct3 == b'110':
                # slti or sltiu -> sub
                alu_op = BitArray(b'1000')
            elif funct3 == b'100' or funct3 == b'101':
                # slli, srli or srai
                alu_op = BitArray(self.funct7[5], 1) + self.funct3
            else:
                alu_op = BitArray(0, 1) + self.funct3

        elif opcode == b'1100011':
            # format B -> on veut toujours faire une soustraction
            alu_op = BitArray(b'1000')

        else:
            # on ne va pas utiliser l'alu, on peut mettre n'importe quoi
            alu_op = BitArray(b'0000')

        return alu_op

    def decode(self, inst):
        """ decode l'instruction inst et retourne le type
        d'instruction décodé.

        Les différents champs décodés dépendent du type d'instruction et sont:
        Decodeur.opcode
        Decodeur.rs1
        Decodeur.rs2
        Decodeur.rd
        Decodeur.funct3
        Decodeur.funct7
        Decodeur.imm
        """

        fmt = Format.fmt(inst)

        self.opcode = Format.opcode(inst)
        self.rd     = Format.rd(inst)
        self.funct3 = Format.funct3(inst)
        self.rs1    = Format.rs1(inst)
        self.rs2    = Format.rs2(inst)
        self.funct7 = Format.funct7(inst)

        if fmt in [Format.I, Format.S, Format.U]:
            self.imm    = Format.imm(inst)
        elif fmt in [Format.SB, Format.UJ]:
            self.imm    = BitArray(b'0') + Format.imm(inst)

        self.alu_op = self.calcul_alu_op()

        return fmt
