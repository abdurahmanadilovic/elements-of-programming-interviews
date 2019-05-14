from unittest import TestCase
from .problem_16_1_tower_of_henoi import solution


class TestSolution(TestCase):
    def testOneItem(self):
        self.assertEqual(1, solution([1], [], []))

    def testTwoItems(self):
        self.assertEqual(3, solution([2, 1], [], []))

    def testThreeItems(self):
        self.assertEqual(7, solution([3, 2, 1], [], []))

    def testFour(self):
        self.assertEqual(15, solution([4, 3, 2, 1], [], []))
