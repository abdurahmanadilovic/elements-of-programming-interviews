from unittest import TestCase
from .problem_7_4_replace_and_remove import *


class TestShift_index_to_end(TestCase):
    def testShifting(self):
        self.assertEqual(['a', 'a', 'b'], shift_b_to_end(['a', 'b', 'a'], 1))

    def testShiftBack(self):
        self.assertEqual(['a', 'b', 'a'], shift_b_to_index(['a', 'a', 'b'], 1))

    def testSolution(self):
        self.assertEqual(['d', 'd', 'c'], solution(['a', 'b', 'c']))

    def testSolution2(self):
        self.assertEqual(['d', 'd', 'c'], solution(['a', 'b', 'c']))
