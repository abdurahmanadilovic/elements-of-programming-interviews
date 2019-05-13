from unittest import TestCase
from .problem_11_1_merge_sorted_files import *


class TestSolution(TestCase):
    def test(self):
        test_case = [
            [3, 5, 7],
            [0, 6, 28],
            [0, 6],
        ]
        self.assertEqual([0, 0, 3, 5, 6, 6, 7, 28], solution(test_case))

    def test2(self):
        test_case = [
            [3, 5, 7, 9, 20],
            [0, 6, 28, 35],
            [1, 2, 3, 4, 55],
        ]
        self.assertEqual([0, 1, 2, 3, 3, 4, 5, 6, 7, 9, 20, 28, 35, 55], solution(test_case))

    def testHeap(self):
        node1 = Node(3)
        node2 = Node(0)
        node3 = Node(1)
        heap = Heap(node1)
        heap.insert(node2)
        heap.insert(node3)
        self.assertEqual(0, heap.take_top())

    def testHeap2(self):
        node1 = Node(0)
        node2 = Node(1)
        node3 = Node(3)
        heap = Heap(node1)
        heap.insert(node2)
        heap.insert(node3)
        self.assertEqual(0, heap.take_top())

    def testHeap3(self):
        node1 = Node(3)
        node2 = Node(0)
        node3 = Node(1)
        heap = Heap(node1)
        heap.insert(node2)
        heap.insert(node3)
        self.assertEqual(0, heap.take_top())
        node1 = Node(5)
        node2 = Node(6)
        node3 = Node(2)
        heap.insert(node1)
        heap.insert(node2)
        heap.insert(node3)
        self.assertEqual(1, heap.take_top())

    def testHeap4(self):
        node1 = Node(3)
        node2 = Node(0)
        node3 = Node(1)
        heap = Heap(node1)
        heap.insert(node2)
        heap.insert(node3)
        node1 = Node(5)
        node2 = Node(6)
        node3 = Node(2)
        heap.insert(node1)
        heap.insert(node2)
        heap.insert(node3)
        pops = []
        while True:
            currentNode = heap.take_top()
            if currentNode is None:
                break
            pops.append(currentNode)
        self.assertEqual([0, 1, 2, 3, 5, 6], pops)

