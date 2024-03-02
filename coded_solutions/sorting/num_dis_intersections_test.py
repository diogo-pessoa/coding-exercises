from unittest import TestCase

from coded_solutions.sorting.num_dis_intersections import solution

class TestNumDiscIntersections(TestCase):
    def test_solution(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)
