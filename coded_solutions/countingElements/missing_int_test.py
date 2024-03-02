from unittest import TestCase

from coded_solutions.countingElements.missing_int import solution_1


class TestMaxCounters(TestCase):
    def test_solution_last_element(self):
        A = [1, 2, 3]
        self.assertEqual(solution_1(A), 4)

    # def test_solution_1_with_example(self):
    #     missing_int = [randint(1, 100) for _ in range(100)]
    #     self.assertEqual(solution_1(missing_int), 5)
    def test_solution_first_positive_from_negative_list(self):
        A = [-1, -2, -3]
        self.assertEqual(solution_1(A), 1)

    def test_solution_empty_list(self):
        A = []
        self.assertEqual(solution_1(A), 1)

    def test_solution_single_element(self):
        A = [5]
        self.assertEqual(solution_1(A), 1)

    def test_solution_single_element_negative(self):
        A = [-5]
        self.assertEqual(solution_1(A), 1)

    def test_solution_single_element_zero(self):
        A = [0]
        self.assertEqual(solution_1(A), 1)

    def test_solution_multiple_elements_missing_middle(self):
        A = [1, 2, 4]
        self.assertEqual(solution_1(A), 3)

    def test_solution_multiple_elements_negative_and_positive(self):
        A = [-1, -2, 1, 2]
        self.assertEqual(solution_1(A), 3)

    def test_solution_multiple_elements_all_negative(self):
        A = [-1, -2, -3]
        self.assertEqual(solution_1(A), 1)