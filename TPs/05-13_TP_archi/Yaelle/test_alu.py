import unittest
from registre import Registre
from bitArray import BitArray
from alu import Alu

class TestAlu(unittest.TestCase):
    def setUp(self):
        self.talu = 32
        self.alu = Alu()

    def test_add(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'0000')

        # addition 5 + 10
        x1 = BitArray(5, nbbits)
        y1 = BitArray(10, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(15, nbbits))
        self.assertFalse(self.alu.carry)
        self.assertFalse(self.alu.overflow)

        # addition 5 + (-6)
        x2 = BitArray(5, nbbits)
        y2 = BitArray(-6, nbbits)
        self.alu.eval(op, x2, y2)
        self.assertEqual(self.alu.res, BitArray(-1, nbbits))
        self.assertFalse(self.alu.overflow)

        # addition -6 + (-2)
        x3 = BitArray(-6, nbbits)
        y3 = BitArray(-2, nbbits)
        self.alu.eval(op, x3, y3)
        self.assertEqual(self.alu.res, BitArray(-8, nbbits))
        self.assertFalse(self.alu.overflow)

        # addition 8 + 8 => carry / overflow
        x4 = BitArray(8, nbbits)
        self.alu.eval(op, x4, x4)
        self.assertEqual(self.alu.res, BitArray(0, nbbits))
        self.assertTrue(self.alu.carry)
        self.assertTrue(self.alu.overflow)

        # addition -8 + (-8) => overflow
        x5 = BitArray(-8, nbbits)
        self.alu.eval(op, x5, x5)
        self.assertEqual(self.alu.res, BitArray(0, nbbits))
        self.assertTrue(self.alu.overflow)

        # tailles différentes
        with self.assertRaises(AssertionError):
            self.alu.eval(op, BitArray(1, 2), BitArray(3, 4))

    def test_sub(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'1000')

        # soustraction 7 - 3
        x1 = BitArray(7, nbbits)
        y1 = BitArray(3, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(4, nbbits))
        self.assertFalse(self.alu.carry)
        self.assertFalse(self.alu.overflow)

        # soustraction 8 - (-3)
        x2 = BitArray(8, nbbits)
        y2 = BitArray(-3, nbbits)
        self.alu.eval(op, x2, y2)
        self.assertEqual(self.alu.res, BitArray(11, nbbits))
        self.assertFalse(self.alu.overflow)

        # soustraction -8 - (-3)
        x3 = BitArray(-8, nbbits)
        y3 = BitArray(-3, nbbits)
        self.alu.eval(op, x3, y3)
        self.assertEqual(self.alu.res, BitArray(-5, nbbits))
        self.assertFalse(self.alu.overflow)

        # soustraction 0 - 5 => carry, !overflow
        x4 = BitArray(0, nbbits)
        y4 = BitArray(5, nbbits)
        self.alu.eval(op, x4, y4)
        self.assertEqual(self.alu.res, BitArray(-5, nbbits))
        self.assertTrue(self.alu.carry)
        self.assertFalse(self.alu.overflow)

        # soustraction -7 - 2 => overflow
        x5 = BitArray(-7, nbbits)
        y5 = BitArray(2, nbbits)
        self.alu.eval(op, x5, y5)
        self.assertEqual(self.alu.res, BitArray(-9, nbbits))
        self.assertTrue(self.alu.overflow)

        # tailles différentes
        with self.assertRaises(AssertionError):
            self.alu.eval(op, BitArray(1, 2), BitArray(3, 4))

    def test_xor(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'0001')

        # b'0101' xor b'1100' = b'1001'
        x1 = BitArray(b'0101')
        y1 = BitArray(b'1100')
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'1001'))

        # tailles différentes
        with self.assertRaises(AssertionError):
            self.alu.eval(op, BitArray(1, 2), BitArray(3, 4))

    def test_bor(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'0011')

        # b'0101' ^ b'1100' = b'1101'
        x1 = BitArray(b'0101')
        y1 = BitArray(b'1100')
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'1101'))

        # tailles différentes
        with self.assertRaises(AssertionError):
            self.alu.eval(op, BitArray(1, 2), BitArray(3, 4))

    def test_band(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'0111')

        # b'0101' xor b'1100' = b'0100'
        x1 = BitArray(b'0101')
        y1 = BitArray(b'1100')
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'0100'))

        # tailles différentes
        with self.assertRaises(AssertionError):
            self.alu.eval(op, BitArray(1, 2), BitArray(3, 4))

    def test_sll(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'0100')

        # b'0100' sll 1 = b'0010'
        # rappel: dans la representation en bytes,
        # les bits de poids faible sont a gauche
        x1 = BitArray(b'0100')
        y1 = BitArray(1, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'0010'))

        # b'0100' sll 4 = b'0000'
        x1 = BitArray(b'0100')
        y1 = BitArray(nbbits, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(0, nbbits))

    def test_srl(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'0101')

        # b'0100' srl 1 = b'1000'
        x1 = BitArray(b'0100')
        y1 = BitArray(1, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'1000'))

        # b'0101' srl 1 = b'1010'
        x1 = BitArray(b'0101')
        y1 = BitArray(1, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'1010'))

    def test_sra(self):
        self.setUp()
        nbbits = 4
        op = BitArray(b'1101')

        # b'0100' srl 1 = b'1000'
        x1 = BitArray(b'0100')
        y1 = BitArray(1, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'1000'))

        # b'0101' srl 1 = b'1011'
        x1 = BitArray(b'0101')
        y1 = BitArray(1, nbbits)
        self.alu.eval(op, x1, y1)
        self.assertEqual(self.alu.res, BitArray(b'1011'))
