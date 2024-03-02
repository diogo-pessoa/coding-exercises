from unittest import TestCase

from coded_solutions.leaders.dominator import solution


class TestDominator(TestCase):
    def test_solution(self):
        A = [3, 4, 3, 2, 3, -1, 3, 3]
        self.assertEqual(3, solution(A))

    def test_solution_from_val(self):
        A= [3, 4, 3, 2, 3, -1, 3, 3]
        self.assertEqual(3, solution(A))
