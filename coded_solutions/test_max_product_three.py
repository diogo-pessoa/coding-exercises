from unittest import TestCase

from coded_solutions.max_product_three import solution


class TestMaxProductThree(TestCase):
    def test_solution(self):
        self.assertEqual(60, solution([-3, 1, 2, -2, 5, 6]))
