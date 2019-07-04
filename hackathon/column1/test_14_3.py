from unittest import TestCase
from .problem_14_3_merge_sort_in_place import solution


class TestSolution(TestCase):
    def testABiggerThanB(self):
        self.assertEqual([1, 2, 3, 4, 5], solution([1, 4, 5, ' ', ' '], [2, 3]))

    def testBBiggerThanA(self):
        self.assertEqual([1, 2, 3, 4, 5], solution([1, 2, 3, ' ', ' '], [4, 5]))

    def testOneByOne(self):
        self.assertEqual([1, 2, 3, 4, 5], solution([1, 3, 5, ' ', ' '], [2, 4]))
