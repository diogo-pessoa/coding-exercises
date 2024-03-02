from unittest import TestCase

from coded_solutions.primeComposite_nums.count_factors import solution


class TestCountFactors(TestCase):
    def test_solution(self):
        N = 24
        self.assertEqual(8, solution(N))
