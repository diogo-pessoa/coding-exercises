from unittest import TestCase

from hackerRank.truckTour.truck_tour import truck_tour


class TestTruckTour(TestCase):
    def test_truck_tour(self):
        self.assertEqual(truck_tour([[1, 5], [10, 3], [3, 4]]), 1)
