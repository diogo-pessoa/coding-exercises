from unittest import TestCase

from coded_solutions.distinct import solution


class TestDistinct(TestCase):
    def test_solution(self):
        self.assertEqual(3, solution([2, 1, 1, 2, 3, 1]))
