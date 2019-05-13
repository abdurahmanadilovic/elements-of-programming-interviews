from unittest import TestCase
from .problem_10_1_balanced_binary_tree import solution, solution2, Node


class TestSolution(TestCase):
    def testNonBalancedCase(self):
        k = Node(7, None, None)
        j = Node(6, None, None)
        i = Node(5, None, None)
        h = Node(4, j, k)
        g = Node(7, None, None)
        f = Node(6, h, i)
        e = Node(5, None, None)
        d = Node(4, None, None)
        c = Node(3, d, e)
        b = Node(2, f, g)
        a = Node(1, b, c)

        self.assertEqual(False, solution(a))
        self.assertEqual(False, solution2(a))

    def testBalancedCase(self):
        k = Node(7, None, None)
        j = Node(6, None, None)
        i = Node(5, None, None)
        h = Node(4, None, None)
        g = Node(7, None, None)
        f = Node(6, h, i)
        e = Node(5, None, None)
        d = Node(4, None, None)
        c = Node(3, d, e)
        b = Node(2, f, g)
        a = Node(1, b, c)

        self.assertEqual(True, solution(a))
        self.assertEqual(True, solution2(a))

