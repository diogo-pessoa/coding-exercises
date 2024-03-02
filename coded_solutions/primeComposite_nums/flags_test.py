from unittest import TestCase

from coded_solutions.primeComposite_nums.flags import solution


class TestFlags(TestCase):
    def test_solution(self):
        A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        self.assertEqual(3, solution(A))
