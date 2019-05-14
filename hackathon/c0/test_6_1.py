from unittest import TestCase
from .problem_6_1_dutch_flag_sorting import solution
import random


class TestSolution(TestCase):
    def testSimpleCase(self):
        n = [4, 5, 3, 1, 2]
        n = solution(n, 2)
        self.validate_condition(n, 3)

    def testAlreadySorted(self):
        n = [1, 2, 3, 4, 5]
        pivot_index = 2
        pivot = n[pivot_index]
        n = solution(n, pivot_index)
        self.validate_condition(n, pivot)

    def testPivotBiggest(self):
        n = [1, 2, 5, 3, 4]
        n = solution(n, 2)
        self.validate_condition(n, 5)

    def testPivotSmallest(self):
        n = [2, 3, 1, 4, 5]
        n = solution(n, 2)
        self.validate_condition(n, 1)

    def testPivotSmallest2(self):
        n = [9, 8, 47, 53, 77]
        n = solution(n, 0)
        self.validate_condition(n, 1)

    def test_random_case(self):
        test_cases = [[random.randint(0, 10) for i in range(10)] for i in range(100000)]
        for test in test_cases:
            n = test
            pivot_index = random.randint(0, 9)
            pivot = n[pivot_index]
            n = solution(n, pivot_index)
            self.validate_condition(n, pivot)

    def validate_condition(self, n, pivot):
        pivot_index = 0
        for index, item in enumerate(n):
            if item == pivot:
                pivot_index = index

        for index in range(len(n)):
            if index < pivot_index:
                self.assertTrue(n[index] <= n[pivot_index])
            if index > pivot_index:
                self.assertTrue(n[index] >= n[pivot_index])
