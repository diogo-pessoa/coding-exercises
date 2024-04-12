import unittest

from coded_solutions.hackerRank.diagonal_diff.diag_diff import diagonalDifference

class TestDiagTest(unittest.TestCase):
    def test_case_1(self):
        arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        self.assertEqual(diagonalDifference(arr), 15)

    def test_case_2(self):
        arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
        self.assertEqual(diagonalDifference(arr), 2)

    def test_case_3(self):
        arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9], [1, 2, 3]]
        self.assertEqual(diagonalDifference(arr), 'Invalid input')

    def test_case_4(self):
        arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9], [1, 2, 3], [1, 2, 3]]
        self.assertEqual(diagonalDifference(arr), 'Invalid input')

    def test_case_5(self):
        arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.assertEqual(diagonalDifference(arr), 'Invalid input')

    def test_case_6(self):
        arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.assertEqual(diagonalDifference(arr), 'Invalid input')

    def test_case_7(self):
        arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
