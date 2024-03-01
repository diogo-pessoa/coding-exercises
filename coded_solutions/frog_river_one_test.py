import random
from unittest import TestCase

from coded_solutions import frog_river_one


class TestFrogRiverOne(TestCase):
    def test_solution(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 5
        frog_river_one.solution_set(X, A)
        self.assertEquals(6, frog_river_one.solution(X, A))

    def test_solution_minus_one_if_no_path_available(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 6
        frog_river_one.solution_set(X, A)
        self.assertEquals(-1, frog_river_one.solution(X, A))

    def test_solution_A_is_empty(self):
        A = []
        X = 6
        frog_river_one.solution_set(X, A)
        self.assertEquals(-1, frog_river_one.solution(X, A))

    def test_solution_many(self):
        A = []
        for i in range(2, 100):
            X = random.randint(1, 100000)
            values = random.sample(range(1, X + 1), X)
            A.append([X, values])
        for X, A in A:
            self.assertEqual(A.index(X), frog_river_one.solution_set(X, A))
