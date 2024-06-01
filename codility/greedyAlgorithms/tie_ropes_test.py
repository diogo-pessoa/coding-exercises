from unittest import TestCase

from codility.greedyAlgorithms.tie_ropes import solution


class TestTieRopes(TestCase):
    def test_solution(self):
        self.assertEqual(3, solution(4, [1, 2, 3, 4, 1, 1, 3]))
