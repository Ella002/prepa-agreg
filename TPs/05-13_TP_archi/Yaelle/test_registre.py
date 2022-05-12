import unittest
from registre import Registre
from bitArray import BitArray

class TestRegistre(unittest.TestCase):
    def test_registre(self):
        nbbits=32
        reg = Registre(nbbits)
        self.assertEqual(reg.bits, BitArray([None]*32))

    def test_ecriture(self):
        nbbits=8
        reg = Registre(nbbits)
        reg.ecriture(BitArray(20, nbbits))
        self.assertEqual(reg.bits, BitArray(20, nbbits))

        with self.assertRaises(TypeError):
            reg.ecriture(BitArray(20, 16))

    def test_lecture(self):
        nbbits = 8
        reg = Registre(nbbits)
        self.assertEqual(reg.lecture(), BitArray(taille=nbbits))

        reg.ecriture(BitArray(20, nbbits))
        self.assertEqual(reg.lecture(), BitArray(20, nbbits))
