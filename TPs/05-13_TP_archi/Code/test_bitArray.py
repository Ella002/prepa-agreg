import unittest
from bitArray import BitArray

class TestBitArray(unittest.TestCase):
    def test_bitarray(self):
        bits= BitArray(taille=8)

        self.assertEqual(bits.bits, [None]*8)


