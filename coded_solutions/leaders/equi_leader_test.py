from unittest import TestCase

from coded_solutions.leaders.equi_leader import findLeader


class TestEquiLeader(TestCase):
    def test_findLeader(self):
        A = [4, 3, 4, 4, 4, 2]
        self.assertEqual(2, findLeader(A))

    def test_findLeader_single(self):
        A = [4]
        self.assertEqual(0, findLeader(A))

