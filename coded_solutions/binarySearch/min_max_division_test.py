from unittest import TestCase

from coded_solutions.binarySearch.min_max_division import solution


class TestMinMAxDivision(TestCase):
    def test_solution(self):
        A = [2, 1, 5, 1, 2, 2, 2]
        K = 3
        M = 5
        self.assertEqual(6, solution(K, M, A))
