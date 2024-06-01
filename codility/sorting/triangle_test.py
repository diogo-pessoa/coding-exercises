from unittest import TestCase

from codility.sorting.triangle import solution

class TestTriangle(TestCase):
    def test_solution(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), 1)

    def test_can_form_triangle_with_positive_numbers(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), 1)

    def test_cannot_form_triangle_with_negative_numbers(self):
        self.assertEqual(solution([-10, -2, -5, -1, -8, -20]), 0)

    def test_cannot_form_triangle_with_zeroes(self):
        self.assertEqual(solution([0, 0, 0]), 0)

    def test_can_form_triangle_with_same_numbers(self):
        self.assertEqual(solution([5, 5, 5]), 1)

    def test_cannot_form_triangle_with_two_numbers(self):
        self.assertEqual(solution([5, 5]), 0)

    def test_cannot_form_triangle_with_one_number(self):
        self.assertEqual(solution([5]), 0)

    def test_cannot_form_triangle_with_empty_list(self):
        self.assertEqual(solution([]), 0)