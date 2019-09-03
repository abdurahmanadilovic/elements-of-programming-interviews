from unittest import TestCase
from .problem_18_7_gasup import solution


class TestSolution(TestCase):
    def testThreeCities(self):
        self.assertEqual(1, solution([[0, 1], [1, 1], [1, 1]]))

    def testThreeCitiesLastCorrect(self):
        self.assertEqual(2, solution([[0, 1], [1, 2], [3, 1]]))
