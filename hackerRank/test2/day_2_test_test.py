import unittest

from hackerRank.test2.day_2_test import *

class TestCountSort(unittest.TestCase):

    def test_case_1(self):
        matrix = [[112, 42, 83, 119],
                  [56, 125, 56, 49],
                  [15, 78, 101, 43],
                  [62, 98, 114, 108]]
        result = 414
        self.assertEqual(flippingMatrix(matrix), result)
    def test_case_2(self):

        matrix = [[112, 42, 83, 119],
                  [56, 125, 56, 49],
                  [15, 78, 101, 43],
                  [62, 98, 114, 108]]
        result = 414
        self.assertEqual(flippingMatrix(matrix), result)
