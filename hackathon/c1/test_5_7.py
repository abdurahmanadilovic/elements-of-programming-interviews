from unittest import TestCase
from .problem_5_7_compute_x_y import solution


class TestSolution(TestCase):
    def testRandomCases(self):
        self.assertEqual(4**4, solution(4, 4))

    def testNegativeCase(self):
        self.assertEqual(4**-4, solution(4, -4))

