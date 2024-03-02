from unittest import TestCase

from coded_solutions.min_bas_sum import solution_1


class TestMinAbsSum(TestCase):
    def test_solution_1(self):
        a = [1, 5, 2, -2]
        self.assertEqual(solution_1(a), 0)

    def test_solution_with_large_numbers(self):
        a = [10000, -5000, 2000, 3000]
        self.assertNotEqual(solution_1(a), 1)