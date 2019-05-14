from unittest import TestCase
from .problem_12_1_search_sorted_array_first_occurrence import solution2 as solution


class TestSolution(TestCase):
    def testSimpleCase(self):
        self.assertEqual(2, solution([1, 2, 3, 3, 100], 3))

    def testSimpleCase2(self):
        self.assertEqual(3, solution([-14, -10, 2, 108, 108, 243, 258, 258, 258, 401], 108))

    def testSimpleCase3(self):
        self.assertEqual(6, solution([-14, -10, 2, 108, 108, 243, 258, 258, 258, 401], 258))
