from unittest import TestCase
from .problem_9_1_stack_max_api import Stack


class TestStack(TestCase):
    def test_single_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())

    def test_multiple_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

    def test_max_api(self):
        stack = Stack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        self.assertEqual(3, stack.max())
        stack.pop()
        self.assertEqual(3, stack.max())
        stack.pop()
        self.assertEqual(3, stack.max())
        stack.pop()
        self.assertEqual(None, stack.max())
