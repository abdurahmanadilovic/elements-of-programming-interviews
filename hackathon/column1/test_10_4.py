from unittest import TestCase
from .problem_10_4_LCA import solution2 as solution, Node


class TestSolution(TestCase):
    def testHeight1(self):
        root = Node(1)
        left = Node(2)
        right = Node(3)

        left.parent = root
        right.parent = root

        self.assertEqual(1, solution(left, right).value)

    def testHeight2(self):
        root = Node(1)
        left = Node(2)
        right = Node(3)
        rightLeft = Node(4)
        rightRight = Node(5)

        left.parent = root
        right.parent = root

        rightLeft.parent = right
        rightRight.parent = right

        self.assertEqual(1, solution(left, rightRight).value)

    def testRootIsNotLCA(self):
        root = Node(1)
        left = Node(2)
        right = Node(3)
        right1 = Node(4)
        left1 = Node(5)
        left1left1 = Node(6)
        left1right1 = Node(7)
        right1left1 = Node(8)
        right1right1 = Node(9)

        left.parent = root
        right.parent = root

        right1.parent = right
        left1.parent = right

        left1left1.parent = left1
        left1right1.parent = left1

        right1left1.parent = right1
        right1right1.parent = right1

        self.assertEqual(3, solution(left1left1, right1right1).value)
