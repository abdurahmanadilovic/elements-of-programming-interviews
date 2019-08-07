from unittest import TestCase
from .problem_6_18_spiral_ordering import *


class TestSolution(TestCase):
    def testTopPrinting(self):
        self.assertEqual([1, 2, 3], print_top([[1, 2, 3]], 0, 0, 3))

    def testBottomPrinting(self):
        self.assertEqual([3, 2, 1], print_bottom([[1, 2, 3]], 0, 0, 3))

    def testRightPrinting(self):
        self.assertEqual([3, 6], print_right_side([[1, 2, 3], [4, 5, 6]], 0, 2, 2))

    def testRightPrinting2(self):
        self.assertEqual([6], print_right_side([[1, 2, 3], [4, 5, 6]], 0, 2, 2))

    def testLeftPrinting(self):
        self.assertEqual([4], print_left_side([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 2, 0))

    def testRecursion(self):
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], solution(array))

    def testRecursion2(self):
        array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        self.assertEqual([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10], solution(array))
