import unittest
from banc_reg import BancRegistre
from bitArray import BitArray

class TestBancRegistre(unittest.TestCase):
    def test_bancregistre(self):
        nbbits=32
        nbregs=32
        banc = BancRegistre(nbregs, nbbits);

