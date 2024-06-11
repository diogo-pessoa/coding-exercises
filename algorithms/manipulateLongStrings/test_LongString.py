import random
from unittest import TestCase

from algorithms.manipulateLongStrings.LongString import LongString


class TestLongString(TestCase):

    def setUp(self):
        print(f"Running test: {self._testMethodName}")

    def test__load_string(self):
        long_string_of_fives = LongString("555555555555")
        self.assertEqual(long_string_of_fives.char_map,
                         {'5': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]})

    def test__load_string_random_vals(self):
        long_string_of_random = LongString("0204050600405060708090")
        self.assertEqual(long_string_of_random.char_map,
                         {'0': [0, 2, 4, 6, 8, 9, 11, 13, 15, 17, 19, 21], '2': [1],
                          '4': [3, 10], '5': [5, 12], '6': [7, 14], '7': [16],
                          '8': [18], '9': [20]})

    def test_longest_substring_compare_equal_strings(self):
        long_string_of_fives = LongString("555555555555")
        self.assertTrue(
            long_string_of_fives.custom_compares(LongString("555555555555")))

    def test_longest_string_compare_unequal_strings(self):
        long_string_of_fives = LongString("555555555555")
        self.assertFalse(
            long_string_of_fives.custom_compares(LongString("555555555556")))

    def test_longest_string_compare_equals_and_custom(self):
        # Initialize the long
        # string, but not used in the static method
        long_string_of_fives = LongString("555555555555")
        string_to_compare = "555555555555"
        self.assertTrue(long_string_of_fives.using_string_comparison(string_to_compare,
                                                                     string_to_compare))

    def test_longest_string_compare_unequals_string_and_custom(self):
        long_string_of_fives = LongString("555555555555")
        string_to_compare = "555555555556"
        self.assertFalse(long_string_of_fives.using_string_comparison("555555555555",
                                                                      string_to_compare))
        self.assertFalse(long_string_of_fives.custom_compares(long_string_of_fives))

    def test_with_random_equals_and_custom(self):
        string_to_compare = str(random.randint(10000000, 1000000000))
        print(string_to_compare)
        long_string_of_random = LongString(string_to_compare)
        self.assertTrue(long_string_of_random.using_string_comparison(string_to_compare,
                                                                      string_to_compare))
        self.assertTrue(
            long_string_of_random.custom_compares(LongString(string_to_compare)))
