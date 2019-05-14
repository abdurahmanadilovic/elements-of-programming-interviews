from unittest import TestCase
from .problem_14_1_intersection_serted_arrays import solution


class TestArrayIntersectionSolution(TestCase):
    def testEdge(self):
        self.assertEqual([], solution([], []))
        self.assertEqual([], solution([1, 2, 3], []))
        self.assertEqual([], solution([], [1, 2, 3]))

    def testSimpleCase(self):
        self.assertEqual([7, 10], solution([5, 7, 10, 11], [1, 2, 6, 7, 10, 15]))

    def testDuplicates(self):
        self.assertEqual([7, 10], solution([5, 7, 7, 10, 11], [1, 2, 6, 7, 7, 7, 10, 15]))

    def testDuplicates2(self):
        self.assertEqual([7, 10], solution([5, 7, 7, 7, 10, 11], [1, 2, 6, 7, 7, 7, 10, 15]))
