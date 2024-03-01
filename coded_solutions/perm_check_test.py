from unittest import TestCase

from coded_solutions.perm_check import solution_improvement, solution_improvement


class TestPermCheck(TestCase):

    def test_solution_linear(self):
        # permutation is the sum of elements in the array len(A) - n(n+1)/2
        A = [4, 1, 3, 2]
        B = [4, 1, 3]

        perms = [A, B]
        self.assertEqual(solution_improvement(perms[0]), 1)
        self.assertEqual(solution_improvement(perms[1]), 0)

    def test_solution_improvement(self):
        # permutation is the sum of elements in the array len(A) - n(n+1)/2
        A = [4, 1, 3, 2]
        B = [4, 1, 3]

        perms = [A, B]
        self.assertEqual(solution_improvement(perms[0]), 1)
        self.assertEqual(solution_improvement(perms[1]), 0)

    def test_solution_improvement_perm(self):
        # permutation is the sum of elements in the array len(A) - n(n+1)/2
        perm = [4, 1, 3, 2]
        self.assertEqual(solution_improvement(perm), 1)


    def test_solution_improvement_check_for_duplicates(self):
        C = [1, 2, 3, 4, 4]
        self.assertEqual(solution_improvement(C), 0)

    def test_solution_improvement_empty_list(self):
        empty = []
        self.assertEqual(solution_improvement(empty), 0)
