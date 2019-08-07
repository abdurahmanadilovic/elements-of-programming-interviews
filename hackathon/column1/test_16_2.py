from unittest import TestCase
from .problem_16_2_non_attacking_queens import solution


class TestSolution(TestCase):
    def testSquareFour(self):
        self.assertEqual([[1, 3, 0, 2], [2, 0, 3, 1]], solution(4))

