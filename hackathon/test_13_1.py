from unittest import TestCase
from .problem_13_1_partition_into_anagrams import solution


class TestSolution(TestCase):
    def testSimpleCase(self):
        self.assertEqual(['debitcard', 'badcredit', 'elvis', 'lives', 'silent', 'listen'],
                         solution(['debitcard', 'badcredit', 'elvis', 'lives', 'silent', 'listen']))
