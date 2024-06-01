from unittest import TestCase

from codility.stacksQueues.fish import solution


class TestFish(TestCase):
    """
        For example, consider arrays A and B such that:
          A[0] = 4    B[0] = 0
          A[1] = 3    B[1] = 1
          A[2] = 2    B[2] = 0
          A[3] = 1    B[3] = 0
          A[4] = 5    B[4] = 0
        Initially all the fish are alive and all except fish number 1 are
        moving
        upstream. Fish number 1 meets fish number 2 and eats it, then it
        meets fish
        number 3 and eats it too. Finally, it meets fish number 4 and is
        eaten by it.
        The remaining two fish, number 0 and 4, never meet and therefore stay
        alive.
        """

    def test_solution(self):
        A = [4, 3, 2, 1, 5]
        B = [0, 1, 0, 0, 0]
        self.assertEqual(2, solution(A, B))

    def test_all_fish_moving_upstream_survive(self):
        A = [4, 3, 2, 1, 5]
        B = [0, 0, 0, 0, 0]
        self.assertEqual(5, solution(A, B))

    def test_all_fish_moving_downstream_survive(self):
        A = [4, 3, 2, 1, 5]
        B = [1, 1, 1, 1, 1]
        self.assertEqual(5, solution(A, B))

    def test_bigger_fish_eats_all_smaller_fish(self):
        A = [1, 2, 3, 4, 5]
        B = [0, 1, 0, 1, 0]
        self.assertEqual(1, solution(A, B))

    def test_smaller_fish_eats_no_fish(self):
        A = [5, 4, 3, 2, 1]
        B = [0, 1, 0, 1, 0]
        self.assertEqual(5, solution(A, B))

    def test_single_fish_survives(self):
        A = [5]
        B = [0]
        self.assertEqual(1, solution(A, B))
