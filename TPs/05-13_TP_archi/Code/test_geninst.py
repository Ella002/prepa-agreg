import unittest
from bitArray import BitArray
from geninst import GenInst
from geninst import table_opcode
from decodeur import Decodeur
from format_inst import Format

class TestGenInst(unittest.TestCase):
    def test_inst(self):
        dec = Decodeur()

        with self.subTest('addi'):
            inst = GenInst.parse_instruction('addi 1,0,987')
            self.assertEqual(dec.decode(inst), Format.I)
            self.assertEqual(dec.opcode,       BitArray(table_opcode['addi']['opcode']))
            self.assertEqual(dec.rd.to_int(),  1)
            self.assertEqual(dec.rs1.to_int(), 0)
            self.assertEqual(dec.funct3,       BitArray(table_opcode['addi']['funct3'], 3))
            self.assertEqual(dec.imm.to_int(), 987)

        with self.subTest('add'):
            inst = GenInst.parse_instruction('add 1,2,3')
            self.assertEqual(dec.decode(inst), Format.R)
            self.assertEqual(dec.opcode,       BitArray(table_opcode['add']['opcode']))
            self.assertEqual(dec.rd.to_int(),  1)
            self.assertEqual(dec.rs1.to_int(), 2)
            self.assertEqual(dec.rs2.to_int(), 3)
            self.assertEqual(dec.funct3,       BitArray(table_opcode['add']['funct3'], 3))
            self.assertEqual(dec.funct7,       BitArray(table_opcode['add']['funct7'], 7))

        with self.subTest('beq'):
            inst = GenInst.parse_instruction('beq 0,0,8190')

            self.assertEqual(dec.decode(inst), Format.SB)
            self.assertEqual(dec.opcode,       BitArray(table_opcode['beq']['opcode']))
            self.assertEqual(dec.rs1.to_int(), 0)
            self.assertEqual(dec.rs2.to_int(), 0)
            self.assertEqual(dec.imm.to_uint(), int(0x1FFE))

        with self.subTest('jal'):
            inst = GenInst.parse_instruction('jal 1,8190')

            self.assertEqual(dec.decode(inst), Format.UJ)
            self.assertEqual(dec.opcode,       BitArray(table_opcode['jal']['opcode']))
            self.assertEqual(dec.rd.to_int(), 1)
            self.assertEqual(dec.imm.to_uint(), int(0x1FFE))

        with self.subTest('lui'):
            inst = GenInst.parse_instruction('lui 1,8190')

            self.assertEqual(dec.decode(inst), Format.U)
            self.assertEqual(dec.opcode,       BitArray(table_opcode['lui']['opcode']))
            self.assertEqual(dec.rd.to_int(), 1)
            self.assertEqual(dec.imm.to_uint(), int(0x1FFE))
