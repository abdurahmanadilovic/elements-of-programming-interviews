from unittest import TestCase
from .problem_9_10_binary_tree_nodes_in_order import solution, Node


class TestSolution(TestCase):
    def testHeight1(self):
        root = Node(1)
        left = Node(2)
        right = Node(3)
        root.left = left
        root.right = right

        self.assertEqual([[1], [2, 3]], solution(root))

    def testHeight2(self):
        root = Node(1)
        left = Node(2)
        right = Node(3)
        leftLeft = Node(4)
        leftRight = Node(5)

        root.left = left
        root.right = right
        left.left = leftLeft
        left.right = leftRight

        self.assertEqual([[1], [2, 3], [4, 5]], solution(root))
