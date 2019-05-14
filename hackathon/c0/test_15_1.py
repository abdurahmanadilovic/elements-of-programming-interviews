from unittest import TestCase
from .problem_15_1_checkBSTProperty import solution, Node


class TestSolution(TestCase):
    def testTreeHeightOne(self):
        left = Node()
        left.value = 1
        right = Node()
        right.value = 11

        root = Node()
        root.value = 10

        root.left = left
        root.right = right

        self.assertEqual(True, solution(root))

    def testTreeHeightOneFalse(self):
        left = Node()
        left.value = 10
        right = Node()
        right.value = 11

        root = Node()
        root.value = 10

        root.left = left
        root.right = right

        self.assertEqual(False, solution(root))

    def testLeftLevelTwoMaxMinTrue(self):
        leftSubLeft = Node()
        leftSubLeft.value = 1
        leftSubRight = Node()
        leftSubRight.value = 9

        left = Node()
        left.value = 2
        left.left = leftSubLeft
        left.right = leftSubRight

        right = Node()
        right.value = 11

        root = Node()
        root.value = 10

        root.left = left
        root.right = right

        self.assertEqual(True, solution(root))

    def testLeftLevelThreeMaxMinFalse(self):
        leftSubLeft = Node()
        leftSubLeft.value = 1
        leftSubRight = Node()
        leftSubRight.value = 9
        leftSubRightLeft = Node()
        leftSubRightLeft.value = 1
        leftSubRight.left = leftSubRightLeft

        left = Node()
        left.value = 2
        left.left = leftSubLeft
        left.right = leftSubRight

        right = Node()
        right.value = 11

        root = Node()
        root.value = 10

        root.left = left
        root.right = right

        self.assertEqual(False, solution(root))
