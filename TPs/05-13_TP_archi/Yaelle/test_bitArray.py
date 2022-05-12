import unittest
from bitArray import BitArray

class TestBitArray(unittest.TestCase):
    def test_bitarray(self):
        bits = BitArray(taille=8)
        self.assertEqual(bits.bits, [None]*8)

    def test_bitarray_int(self):
        bits = BitArray(5, 3)
        self.assertEqual(bits.bits, [True, False, True])

        bits = BitArray(3, 3)
        self.assertEqual(bits.bits, [True, True, False])

        bits = BitArray(5, 32)
        self.assertEqual(bits.bits, [True, False, True]+[False]*29)

        bits = BitArray(-1, 3)
        self.assertEqual(bits.bits, [True]*3)

    def test_bitarray_bytes(self):
        bits = BitArray(b'110')
        self.assertEqual(bits.bits, [True, True, False])

        bits = BitArray(b'X10')
        self.assertEqual(bits.bits, [None, True, False])

        with self.assertRaises(ValueError):
            bits = BitArray(b'a10')

    def test_read_bit(self):
        bits = BitArray(b'1X0')

        self.assertTrue(bits[0])
        self.assertIsNone(bits[1])
        self.assertFalse(bits[-1])
        with self.assertRaises(IndexError):
            bits[3]

    def test_write_bit(self):
        bits = BitArray(b'110')

        bits[0] = False
        self.assertEqual(bits.bits, [False, True, False])

        bits[1] = None
        self.assertEqual(bits.bits, [False, None, False])

        # on peut accéder au dernier bit, mais pas le modifier
        with self.assertRaises(IndexError):
            bits[-1] = True

    def test_read_bits(self):
        bits = BitArray(b'11001')

        self.assertEqual(bits[1:3].bits, [True, False])
        self.assertEqual(bits[3:].bits, [False, True])
        # bits[:3] renvoie TypeError
        with self.assertRaises(IndexError):
            bits[2:0]
        self.assertEqual(bits[0:0].bits, [])

    def test_concat(self):
        b1 = BitArray(b'1')
        b2 = BitArray(b'0')

        self.assertEqual((b1+b2).bits, [True, False])

    def test_len(self):
        self.assertEqual(len(BitArray(b'110')), 3)
        self.assertEqual(len(BitArray(5, 3)), 3)
        self.assertEqual(len(BitArray(b'')), 0)

    def test_toint(self):
        b_pos = BitArray(b'1010')
        self.assertEqual(b_pos.to_int(), 5)

        b_neg = BitArray(b'1011')
        self.assertEqual(b_neg.to_int(), -3)

        b_undef = BitArray(b'XXX')
        with self.assertRaises(TypeError):
            b_undef.to_int()

    def test_touint(self):
        b_pos = BitArray(b'1010')
        self.assertEqual(b_pos.to_uint(), 5)

        b_neg = BitArray(b'1011')
        self.assertEqual(b_neg.to_uint(), 13)

        b_undef = BitArray(b'XXX')
        with self.assertRaises(TypeError):
            b_undef.to_uint()

    def test_tobytes(self):
        bits = BitArray(20, 5)
        self.assertEqual(bits.to_bytes(), b'00101')

        bits = BitArray(3, 3)
        bits[2] = None
        self.assertEqual(bits.to_bytes(), b'11X')
