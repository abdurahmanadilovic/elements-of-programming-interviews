from unittest import TestCase
from .problem_8_2_reverse_singly_linked_list import solution, Node


class TestSolution(TestCase):
    def testBasicCase(self):
        root = Node(1)
        node2 = Node(2)
        root.next = node2
        node3 = Node(3)
        node2.next = node3

        newRoot = solution(root)
        self.assertEqual(3, newRoot.value)
        self.assertEqual(2, newRoot.next.value)
        self.assertEqual(1, newRoot.next.next.value)
