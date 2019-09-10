from unittest import TestCase
from .problem_19_8_transform_strings import solution, calculate_cost


class TestSolution(TestCase):
    def testGivenCase(self):
        self.assertEqual(4, solution(['bat', 'cot', 'dog', 'dag', 'dot', 'cat'], 'cat', 'dog'))

    def testSimpleCase(self):
        self.assertEqual(3, solution(['aab', 'aac', 'bad', 'aad', 'bad', 'cat'], 'aab', 'bad'))

    def testDiff(self):
        self.assertEqual(0, calculate_cost('a', 'a'))

    def testDiff2(self):
        self.assertEqual(1, calculate_cost('a', 'b'))

    def testDiff3(self):
        # cat <-> cot
        self.assertEqual(1, calculate_cost('cat', 'cot'))
