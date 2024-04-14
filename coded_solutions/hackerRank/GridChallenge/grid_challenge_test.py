from unittest import TestCase

from coded_solutions.hackerRank.GridChallenge.grid_challenge import gridChallenge


class TestGridChallenge(TestCase):
    def test_grid_challenge_in_order(self):
        self.assertEqual(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']), 'YES')

    def test_grid_challenge_not_ordered_in_columns(self):
        self.assertEqual(gridChallenge(['ebacd', 'olmkn', 'fghij', 'trpqs', 'xywuv']), 'NO')