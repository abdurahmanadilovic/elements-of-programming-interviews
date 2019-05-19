from unittest import TestCase
from .problem_8_4_detect_cycle import solution, Node


class TestSolution(TestCase):
    def testNoCycle(self):
        self.assertEqual(None, solution(Node(2)))

    def testCycleLength1(self):
        root = Node(1)
        second = Node(2)
        root.next = second
        second.next = root
        self.assertEqual(1, solution(root).value)

    def testCycleLength2(self):
        root = Node(1)
        second = Node(2)
        third = Node(3)
        root.next = second
        second.next = third
        third.next = root
        self.assertEqual(1, solution(root).value)

    def testCycleNotAtRoot(self):
        root = Node(1)
        second = Node(2)
        third = Node(3)
        root.next = second
        second.next = third
        third.next = second
        self.assertEqual(2, solution(root).value)
