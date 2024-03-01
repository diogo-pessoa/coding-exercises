from random import sample
from unittest import TestCase

from tape_equilibrium import solution_linear


class TapeEquilibriumTest(TestCase):
    # A = [[3, 1, 2, 4, 3]]

    def test_solution_linear(self):
        A = [[3, 1, 2, 4, 3], [3, 2, 4, 5, 6, 7, 8, 3, 5, 2]]
        print(solution_linear(A[1]))
        self.assertEqual(solution_linear(A[0]), 1)
        self.assertEqual(solution_linear(A[1]), 5)

    def test_solution_linear_simple_negative(self):
        A = [[3, 1, 2, 4, 3], [3, 2, 4, -5, -6, 7, 8, 3, 5, -2]]
        for i in range(2, 100000):
            values = sample(range(-1000, 1000), 30)
            A.append(values)
        self.assertEqual(solution_linear(A[1]), 1)
