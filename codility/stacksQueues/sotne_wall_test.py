from unittest import TestCase

from codility.stacksQueues.sotne_wall import solution


class TestStoneWall(TestCase):
    def test_solution_3(self):
        H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
        self.assertEqual(7, solution(H))
