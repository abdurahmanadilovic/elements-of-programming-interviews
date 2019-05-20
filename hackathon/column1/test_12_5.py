from unittest import TestCase
from .problem_12_5_closes_squared_number import solution


class TestSolution(TestCase):
    def testGivenCases(self):
        self.assertEqual(4, solution(16))

    def testGivenCases2(self):
        self.assertEqual(17, solution(300))

    def testZero(self):
        self.assertEqual(0, solution(0))

    def testOne(self):
        self.assertEqual(1, solution(1))

    def testTwo(self):
        self.assertEqual(1, solution(2))
