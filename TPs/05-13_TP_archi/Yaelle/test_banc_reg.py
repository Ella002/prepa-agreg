import unittest
from banc_reg import BancRegistre
from bitArray import BitArray

class TestBancRegistre(unittest.TestCase):
    def test_bancregistre(self):
        nbbits = 32
        nbregs = 32
        banc = BancRegistre(nbregs, nbbits)

        # registre 0 = 0
        self.assertEqual(banc[0], BitArray([False]*nbbits))
        # registre n = XXXXX
        self.assertEqual(banc[2], BitArray([None]*nbbits))

    def test_ecriture(self):
        nbbits = 8
        nbregs = 8
        banc = BancRegistre(nbregs, nbbits)

        bits = BitArray(20, nbbits)

        # on ecrit en registre quelconque
        banc.ecriture(1, bits)
        self.assertEqual(banc[1], BitArray(20, nbbits))

        # on ecrit au registre 0
        banc.ecriture(0, bits)
        self.assertEqual(banc[0], BitArray(0, nbbits))

        # on ecrit en dehors du banc
        with self.assertRaises(IndexError):
            banc.ecriture(nbregs+1, bits)

    def test_lecture(self):
        nbbits = 8
        nbregs = 8
        banc = BancRegistre(nbregs, nbbits)

        # on lit les registres 0 et 2
        self.assertEqual(banc.lecture(0), BitArray(0, nbbits))
        self.assertEqual(banc.lecture(2), BitArray([None]*nbbits))
