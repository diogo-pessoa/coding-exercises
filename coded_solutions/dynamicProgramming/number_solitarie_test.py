from unittest import TestCase

from coded_solutions.dynamicProgramming.number_solitarie import solution_ns


class TestNumberSolitarie(TestCase):
    def test_solution_ns(self):
        self.assertEqual(solution_ns([1, -2, 0, 9 - 1, -2]), 8)
