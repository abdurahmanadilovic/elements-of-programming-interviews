from unittest import TestCase
from .problem_17_2_levensheiten_distance import solution


class TestSolution(TestCase):
    def testSame(self):
        self.assertEqual(0, solution('a', 'a'))

    def testLength1(self):
        self.assertEqual(1, solution('a', 'b'))

    def testLength2(self):
        self.assertEqual(2, solution('aa', 'b'))

    def testLength2prefix(self):
        self.assertEqual(1, solution('ba', 'b'))

    def testLength2suffix(self):
        self.assertEqual(1, solution('ab', 'b'))

    def testInTheMiddle(self):
        self.assertEqual(1, solution('aab', 'abb'))

    def testOneEmpty(self):
        self.assertEqual(3, solution('', 'abb'))

    def testTargetEmpty(self):
        self.assertEqual(2, solution('aa', ''))

    def testGivenCase(self):
        self.assertEqual(8, solution('Carthorse', 'Orchestra'))
