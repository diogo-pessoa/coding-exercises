from unittest import TestCase

from coded_solutions.caterpillarMethod.count_distinct_slices import solution

class TestCountDistinctSlices(TestCase):
    def test_solution(self):
        A = [3, 4, 5, 5, 2]
        self.assertEqual(9, solution(6, A))

    def test_solution_empty(self):
        A = []
        self.assertEqual(0, solution(1, A))

    def test_solution_single(self):
        A = [1]
        self.assertEqual(1, solution(1, A))

    def test_solution_single_max(self):
        A = [1000000000]
        self.assertEqual(1, solution(1, A))
