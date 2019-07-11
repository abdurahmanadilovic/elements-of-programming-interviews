from unittest import TestCase
from .problem_15_4_largest_k_values_bst import solution, Node


class TestSolution(TestCase):
    def testSimpleCase(self):
        leftRightLeft = Node()
        leftRightLeft.value = 29

        leftRight = Node()
        leftRight.value = 37
        leftRight.left = leftRightLeft

        left = Node()
        left.value = 23
        left.right = leftRight

        right = Node()
        right.value = 43
        right.left = left

        root = Node()
        root.value = 19
        root.right = right

        self.assertEqual([43, 37, 29], solution(root, 3))
