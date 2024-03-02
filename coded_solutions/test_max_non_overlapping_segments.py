from unittest import TestCase

from coded_solutions.max_non_overlapping_segments import solution


class TestMaxNonOverlappingSegments(TestCase):
    def test_solution(self):
        A = [1, 3, 7, 9, 9]
        B = [5, 6, 8, 9, 10]
        self.assertEqual(solution(A, B), 3)
