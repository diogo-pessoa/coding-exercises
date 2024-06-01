from unittest import TestCase

from codility.maximumSliceProblem.max_double_slice_sum import solution


class TestMaxDoubleSliceSum(TestCase):
    def test_solution(self):
        A = [3, 2, 6, -1, 4, 5, -1, 2]
        self.assertEqual(17, solution(A))
