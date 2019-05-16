from unittest import TestCase
from .problem_7_2_base_conversioni import *


class TestSolution(TestCase):
    def testToDecimal(self):
        self.assertEqual(306, base_to_decimal('615', 7))

    def testToDecimalWithA(self):
        self.assertEqual(306, base_to_decimal('1A7', 13))

    def testNegativeBase(self):
        self.assertEqual(306, base_to_decimal('-1A7', 13))

    def testGivenCase(self):
        self.assertEqual('1A7', solution('615', 7, 13))

    def testNegative(self):
        self.assertEqual('-1A7', solution('-615', 7, 13))
