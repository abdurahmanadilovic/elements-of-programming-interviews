from unittest import TestCase
from .problem_12_9_k_largest import solution, partition_around_index


class TestSolution(TestCase):
    def testPartition(self):
        self.assertEqual(0, partition_around_index(0, 1, 1, [2, 1]))

    def testPartition2(self):
        self.assertEqual(1, partition_around_index(0, 1, 1, [1, 2]))

    def testPartition3(self):
        self.assertEqual(2, partition_around_index(0, 4, 0, [3, 2, 1, 5, 4]))

    def testBasicCase(self):
        for i in range(1, 6):
            result = solution([3, 2, 1, 5, 4], i)
            self.assertEqual(i, result)

