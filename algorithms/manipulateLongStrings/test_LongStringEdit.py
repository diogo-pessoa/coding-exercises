import unittest

from algorithms.manipulateLongStrings.LongString import LongString


class LongStringEdit(unittest.TestCase):

    def setUp(self):
        print(f"Running test: {self._testMethodName}")

    @unittest.skip("TODO - Not Implemented")
    def test_edit(self):
        long_string_of_fives = LongString("555555555555")
        self.assertTrue(long_string_of_fives.edit())
