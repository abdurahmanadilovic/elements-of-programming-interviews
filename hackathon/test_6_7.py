from unittest import TestCase
from .problem_6_7_buy_sell_stock_once import *


class TestSolution(TestCase):
    def testGivenCase(self):
        self.assertEqual(30, solution([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

    def testEmpty(self):
        self.assertEqual(0, solution([]))

    def testOne(self):
        self.assertEqual(0, solution([1]))

    def testTwo(self):
        self.assertEqual(1, solution([1, 2]))

    def testVariant(self):
        self.assertEqual(3, solution_variant([1, 1, 2, 3, 4, 5, 7, 7, 7]))

    def testVariant2(self):
        self.assertEqual(2, solution_variant([1, 1, 2, 3, 4, 5, 7, 7]))

    def testVariant3(self):
        self.assertEqual(4, solution_variant([0, 0, 1, 1, 1, 1, 4, 5, 7, 7]))
