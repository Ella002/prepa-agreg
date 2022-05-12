import unittest
from format_inst import Format
from bitArray import BitArray

class TestFormat(unittest.TestCase):
    def test_format(self):
        #        opcode  rd  funct3 rs1   rs2    funct7
        inst = BitArray(b'11110110001000000001000110000000')
        self.assertEqual(Format.fmt(inst),    Format.UJ)
        self.assertEqual(Format.opcode(inst), BitArray(b'1111011'))
        self.assertEqual(Format.rd(inst),     BitArray(b'00010'))
        self.assertEqual(Format.rs1(inst),    BitArray(b'00001'))
        self.assertEqual(Format.rs2(inst),    BitArray(b'00011'))
        self.assertEqual(Format.funct3(inst), BitArray(b'000'))
        self.assertEqual(Format.funct7(inst), BitArray(b'0000000'))
        self.assertEqual(Format.imm(inst),    BitArray(b'00110000000000000010'))

