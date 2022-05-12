import unittest
from decodeur import Decodeur, Format
from bitArray import BitArray
from registre import Registre

class TestDecodeur(unittest.TestCase):
    def setUp(self):
        self.IR = Registre(32)  # le registre d'instruction
        self.dec = Decodeur()

    def test_decode_formatR(self):
        with self.subTest(op='add'):
            # test format R
            # add R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'000'
            funct7 = b'0000000'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.opcode, BitArray(op))
            self.assertEqual(self.dec.rd,     BitArray(rd))
            self.assertEqual(self.dec.rs1,    BitArray(rs1))
            self.assertEqual(self.dec.rs2,    BitArray(rs2))
            self.assertEqual(self.dec.funct3, BitArray(funct3))
            self.assertEqual(self.dec.funct7, BitArray(funct7))

            self.assertEqual(self.dec.alu_op, BitArray(b'0000'))

        with self.subTest(op='sub'):
            # test format R avec funct7
            # sub R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'000'
            funct7 = b'0000010'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.alu_op, BitArray(b'1000'))

        with self.subTest(op='xor'):
            # xor R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'001'
            funct7 = b'0000000'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.alu_op, BitArray(b'0001'))

        with self.subTest(op='or'):
            # or R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'011'
            funct7 = b'0000000'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.alu_op, BitArray(b'0011'))

        with self.subTest(op='and'):
            # and R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'111'
            funct7 = b'0000000'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.alu_op, BitArray(b'0111'))

        with self.subTest(op='sll'):
            # sll R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'100'
            funct7 = b'0000000'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.alu_op, BitArray(b'0100'))

        with self.subTest(op='srl'):
            # srl R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'101'
            funct7 = b'0000000'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.alu_op, BitArray(b'0101'))

        with self.subTest(op='sra'):
            # sra R2 R3 R1
            op     = b'1100110'
            rd     = b'10000'
            rs1    = b'01000'
            rs2    = b'11000'
            funct3 = b'101'
            funct7 = b'0000010'
            inst = BitArray(op + rd + funct3 + rs1 + rs2 + funct7)

            self.assertEqual(self.dec.decode(inst), Format.R)
            self.assertEqual(self.dec.alu_op, BitArray(b'1101'))

    def test_decode_formatI(self):
        with self.subTest(op='addi'):
            # addi R2 R3 0b100000000000
            op     = b'1100100'
            rd     = b'10000'
            rs1    = b'01000'
            funct3 = b'000'
            imm    = b'100000000000'
            inst = BitArray(op + rd + funct3 + rs1 + imm)

            self.assertEqual(self.dec.decode(inst), Format.I)
            self.assertEqual(self.dec.alu_op, BitArray(b'0000'))

        with self.subTest(op='xori'):
            # xori R2 R3 0b100000000000
            op     = b'1100100'
            rd     = b'10000'
            rs1    = b'01000'
            funct3 = b'001'
            imm    = b'100000000000'
            inst = BitArray(op + rd + funct3 + rs1 + imm)

            self.assertEqual(self.dec.decode(inst), Format.I)
            self.assertEqual(self.dec.alu_op, BitArray(b'0001'))

        with self.subTest(op='ori'):
            # ori R2 R3 0b100000000000
            op     = b'1100100'
            rd     = b'10000'
            rs1    = b'01000'
            funct3 = b'011'
            imm    = b'100000000000'
            inst = BitArray(op + rd + funct3 + rs1 + imm)

            self.assertEqual(self.dec.decode(inst), Format.I)
            self.assertEqual(self.dec.alu_op, BitArray(b'0011'))

        with self.subTest(op='andi'):
            # andi R2 R3 0b100000000000
            op     = b'1100100'
            rd     = b'10000'
            rs1    = b'01000'
            funct3 = b'111'
            imm    = b'100000000000'
            inst = BitArray(op + rd + funct3 + rs1 + imm)

            self.assertEqual(self.dec.decode(inst), Format.I)
            self.assertEqual(self.dec.alu_op, BitArray(b'0111'))

        with self.subTest(op='slli'):
            # slli R2 R3 0b100000000010
            op     = b'1100100'
            rd     = b'10000'
            rs1    = b'01000'
            funct3 = b'100'
            imm    = b'100000000000'
            inst = BitArray(op + rd + funct3 + rs1 + imm)

            self.assertEqual(self.dec.decode(inst), Format.I)
            self.assertEqual(self.dec.alu_op, BitArray(b'0100'))

        with self.subTest(op='srli'):
            # srli R2 R3 0b100000000010
            op     = b'1100100'
            rd     = b'10000'
            rs1    = b'01000'
            funct3 = b'101'
            imm    = b'100000000000'
            inst = BitArray(op + rd + funct3 + rs1 + imm)

            self.assertEqual(self.dec.decode(inst), Format.I)
            self.assertEqual(self.dec.alu_op, BitArray(b'0101'))

        with self.subTest(op='srai'):
            # srai R2 R3 0b100000000010
            op     = b'1100100'
            rd     = b'10000'
            rs1    = b'01000'
            funct3 = b'101'
            imm    = b'100000000010'
            inst = BitArray(op + rd + funct3 + rs1 + imm)

            self.assertEqual(self.dec.decode(inst), Format.I)
            self.assertEqual(self.dec.alu_op, BitArray(b'1101'))

    def test_decode_formatB(self):
        # test format B
        # beq R1 R2 0b100000000000
        op      = b'1100011'
        rs1     = b'10000'
        rs2     = b'10000'
        funct3  = b'000'
        imm1_4  = b'1000'
        imm5_10 = b'000000'
        imm11   = b'0'
        imm12   = b'0'
        inst = BitArray(op + imm11 + imm1_4 + funct3 + rs1 + rs2 + imm5_10 + imm12)

        self.assertEqual(self.dec.decode(inst), Format.SB)
        self.assertEqual(self.dec.alu_op, BitArray(b'1000'))

    def test_decode_formatS(self):
        # test format S
        # sw rs1 rs2 010101010101
        op     = b'1100010'
        rs1    = b'00010'
        rs2    = b'00011'
        funct3 = b'010'
        imm    = b'010101010101'
        inst = BitArray(op + imm[0:5] +funct3 + rs1 + rs2 + imm[5:12])
