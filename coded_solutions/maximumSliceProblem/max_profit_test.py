from unittest import TestCase

from coded_solutions.maximumSliceProblem.max_profit import solution


class TestMaxProfit(TestCase):
    def test_solution(self):
        A = [23171, 21011, 21123, 21366, 21013, 21367]
        self.assertEqual(356, solution(A))

    def test_solution_single(self):
        A = [23171, 21011, 21123, 21366, 21013, 21367]
        self.assertEqual(356, solution(A))
