from unittest import TestCase
from .problem_5_1_word_parity import solution


class TestSolution(TestCase):
    def testFive(self):
        self.assertEqual(0, solution(5))

    def testEleven(self):
        self.assertEqual(1, solution(11))

    def testZero(self):
        self.assertEqual(0, solution(0))

    def testOne(self):
        self.assertEqual(1, solution(1))

    def testBig(self):
        self.assertEqual(1, solution(256))

    def testBig2(self):
        self.assertEqual(0, solution(255))

    def testBig3(self):
        self.assertEqual(1, solution(256256))

    def testLargeCases(self):
        test_word = 1 << 127 | 1 << 63 | 1 << 7
        self.assertEqual(1, solution(test_word))

    def testLargeCases2(self):
        test_word = 1 << 63 | 1 << 15 | 1 << 7
        self.assertEqual(1, solution(test_word))

    def testLargeCases3(self):
        test_word = 1 << 63 | 1 << 15
        self.assertEqual(0, solution(test_word))
