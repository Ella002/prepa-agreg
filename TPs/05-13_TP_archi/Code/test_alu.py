import unittest
from registre import Registre
from bitArray import BitArray
from alu import Alu

class TestAlu(unittest.TestCase):
    def setUp(self):
        self.talu = 32
        self.alu = Alu()

