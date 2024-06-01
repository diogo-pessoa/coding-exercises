from unittest import TestCase

from codility.min_avg_two_slice import solution


class TestMinAvgTwoSlice(TestCase):
    def test_solution(self):
        A = [4, 2, 2, 5, 1, 5, 8]
        self.assertEqual(1, solution(A))
