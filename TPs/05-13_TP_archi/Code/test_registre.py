import unittest
from registre import Registre
from bitArray import BitArray

class TestBancRegistre(unittest.TestCase):
    def test_bancregistre(self):
        nbbits=32
        nbregs=32
        reg = Registre(nbbits);

