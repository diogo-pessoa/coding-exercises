from unittest import TestCase

from coded_solutions.maximumSliceProblem.max_slice_sum import solution


class TestMaxSliceSum(TestCase):
    def test_seolution(self):
        A = [3, 2, -6, 4, 0]
        self.assertEqual(5, solution(A))
