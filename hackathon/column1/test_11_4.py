from unittest import TestCase
from .problem_11_4_k_closest_stars import *


class TestSolution(TestCase):
    def testThreeStarts(self):
        self.assertEqual([13, 8, 3], solution([Star(1, 2, 3), Star(4, 5, 6), Star(7, 8, 9)], 3))

    def testKSmallerThanN(self):
        self.assertEqual([8, 3, 1], solution([Star(1, 2, 3), Star(4, 5, 6), Star(7, 8, 9), Star(1, 1, 1)], 3))
