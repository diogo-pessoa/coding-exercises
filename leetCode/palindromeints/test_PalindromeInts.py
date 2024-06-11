import random
from unittest import TestCase

from leetCode.palindromeints.PalindromeInts import PalindromeInts


class TestPalindromeInts(TestCase):

    def setUp(self):
        # Print the name of the currently running test
        print(f"Running test: {self._testMethodName}")
        self.palindrome_nums = PalindromeInts()
        rand_int = random.randint(10000, 1000000000)  # larger random number
        rand_int_smaller = random.randint(0, 1000)
        self.palindrome_rand = self.palindrome_nums.make_palindrome(rand_int)
        self.palindrome_rand_smaller = self.palindrome_nums.make_palindrome(
            rand_int_smaller)

    def test_palindrome(self):
        print(f"int to check: {self.palindrome_rand}")
        self.assertEqual(self.palindrome_nums.is_palindrome_int(-121), False)
        self.assertEqual(self.palindrome_nums.is_palindrome_int(1), True)
        self.assertEqual(self.palindrome_nums.is_palindrome_int(0), True)
        self.assertEqual(self.palindrome_nums.is_palindrome_int(121), True)

    def test_palindrome_str(self):
        print(f"int to check: {self.palindrome_rand}")
        self.assertEqual(self.palindrome_nums.is_palindrome_str(self.palindrome_rand),
                         False)
        self.assertEqual(self.palindrome_nums.is_palindrome_str(-121), True)
        self.assertEqual(self.palindrome_nums.is_palindrome_str(0), True)

    def test_palindrome_large_ints(self):
        print(f"int to check: {self.palindrome_rand}")
        self.assertEqual(self.palindrome_nums.is_palindrome_int(self.palindrome_rand),
                         True)
        self.assertEqual(self.palindrome_nums.is_palindrome_str(self.palindrome_rand),
                         True)
        self.assertEqual(
            self.palindrome_nums.is_palindrome_x_declared(self.palindrome_rand), True)

    def test_palindrome_small_ints(self):
        print(f"int to check: {self.palindrome_rand_smaller}")
        print(self.palindrome_rand_smaller)
        self.assertEqual(
            self.palindrome_nums.is_palindrome_int(self.palindrome_rand_smaller), True)
        self.assertEqual(
            self.palindrome_nums.is_palindrome_str(self.palindrome_rand_smaller), True)
        self.assertEqual(
            self.palindrome_nums.is_palindrome_x_declared(self.palindrome_rand_smaller),
            True)
