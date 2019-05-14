from unittest import TestCase
from .problem_19_2_search_maze import solution2 as solution


class TestSolution(TestCase):
    def testEmptyCase(self):
        self.assertEqual(False, solution([]))

    def testOneMove(self):
        self.assertEqual(True, solution([['c', 'e']]))

    def testOneWall(self):
        self.assertEqual(False, solution([[' ', 'w', 'e']]))

    def testTwoRows(self):
        self.assertEqual(True, solution([[' ', 'w', 'e'], ['', '', '']]))

    def testTwoRowsNoPath(self):
        self.assertEqual(False, solution([[' ', 'w', 'e'], ['', 'w', '']]))
