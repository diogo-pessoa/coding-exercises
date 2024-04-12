from unittest import TestCase

from coded_solutions.hackerRank.towerBreakers.tower_breakers import *

class TestTowerBreakers(TestCase):
    def test_tower_breakers(self):

        self.assertEqual(towerBreakers(2, 6), 2)

    def test_tower_breakers_m_four(self):
        self.assertEqual(towerBreakers(1, 4), 1)

    def test_tower_breakers_m_odds(self):
        self.assertEqual(towerBreakers(3, 7), 1)
    def test_tower_breakers_m_odds(self):
            self.assertEqual(towerBreakers(1, 7), 1)
