from unittest import TestCase
from .problem_13_3_anonymous_letter import solution


class TestSolution(TestCase):
    def testBasicCase(self):
        self.assertEqual(True, solution('abc', 'abcccd'))
