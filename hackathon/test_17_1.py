from unittest import TestCase
from .problem_17_1_score_combinations import solution


class TestSolve(TestCase):
    def testSimpleCase(self):
        self.assertEqual(1, solution(3))
        self.assertEqual(1, solution(2))

    def testSeven(self):
        self.assertEqual(2, solution(7))

    def testSimpleCase2(self):
        self.assertEqual(2, solution(6))

    def testSimpleCase3(self):
        self.assertEqual(3, solution(10))

    def testSimpleCase4(self):
        self.assertEqual(4, solution(13))

    def testSimpleCase5(self):
        self.assertEqual(4, solution(12))
