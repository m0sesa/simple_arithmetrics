import unittest
from src.mathematics.arithmetric import Arithmetrics

class TestArithmetrics(unittest.TestCase):

    def setUp(self) -> None:
        self.arithmetric = Arithmetrics()
        return super().setUp()

    def test_sum(self):
        self.assertEqual(self.arithmetric.sum(2,2), 4)

    def test_divide(self):
        self.assertEqual(self.arithmetric.divide(4,2), 2)
        with self.assertRaises(ZeroDivisionError):
            self.arithmetric.divide(3,0)

    def test_multiplicaton(self):
        self.assertEqual(self.arithmetric.multiply(3,32), 96)