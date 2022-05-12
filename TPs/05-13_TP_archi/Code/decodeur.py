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

    Lève une exception InstructionInconue() si le format de l'instruction n'est pas reconue
    """
    def calcul_alu_op(self):
        """
        retroune le code opération de l'alu en fonction de l'instruction courante
        """
        opcode = self.opcode.to_bytes()

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
