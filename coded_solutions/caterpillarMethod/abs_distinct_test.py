from unittest import TestCase

from coded_solutions.caterpillarMethod.abs_distinct import solution

class TestAbsDistinct(TestCase):
    def test_solution(self):
        self.assertEqual(5, solution([-5, -3, -1, 0, 3, 6]))
