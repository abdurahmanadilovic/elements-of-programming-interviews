from unittest import TestCase
from .problem_18_5_three_sum import solution


class TestSolution(TestCase):
    def testGivenCase(self):
        self.assertEqual(True, solution([2, 3, 5, 7, 11], 21))

    def testNoSolution(self):
        # 2 + 2 + 5 = 4 + 5 = 9
        self.assertEqual(True, solution([2, 3, 5, 7, 11], 9))
