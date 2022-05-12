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

    def test_decode_formatS(self):
        # test format S
        # sw rs1 rs2 010101010101
        op     = b'1100010'
        rs1    = b'00010'
        rs2    = b'00011'
        funct3 = b'010'
        imm    = b'010101010101'
        inst = BitArray(op + imm[0:5] +funct3 + rs1 + rs2 + imm[5:12])

