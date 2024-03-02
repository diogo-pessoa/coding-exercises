from unittest import TestCase

from coded_solutions.countingElements.max_counters import solution_2, solution_1


class TestMaxCounters(TestCase):
    def test_solution_2(self):
        A = [3, 4, 4, 6, 1, 4, 4]
        self.assertEqual(solution_2(5, A), [3, 2, 2, 4, 2])

    def test_solution_2_empty(self):
        A = []
        self.assertEqual(solution_2(5, A), [])

    def test_solution_2_single(self):
        A = [1]
        self.assertEqual(solution_2(1, A), [1])

    def test_solution_2_single_max(self):
        A = [6]
        self.assertEqual(solution_2(1, A), [0])

    def test_solution_2(self):
        B = [3, 4, 4, 6, 1, 4, 4]
        self.assertNotEquals(solution_2(6, B), [3, 2, 2, 4, 2])

    def test_solution_1(self):
        A = [3, 4, 4, 6, 1, 4, 4]
        self.assertEqual(solution_1(5, A), [3, 2, 2, 4, 2])

    def test_solution_1_empty(self):
        A = []
        self.assertEqual(solution_1(5, A), [])

    def test_solution_1_single(self):
        A = [1]
        self.assertEqual(solution_1(1, A), [1])

    def test_solution_1_single_max(self):
        A = [6]
        self.assertEqual(solution_1(1, A), [0])

    def test_solution_1(self):
        B = [3, 4, 4, 6, 1, 4, 4]
        self.assertNotEqual(solution_1(6, B), [3, 2, 2, 4, 2])