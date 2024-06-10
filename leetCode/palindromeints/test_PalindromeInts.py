from unittest import TestCase

from leetCode.palindromeints.PalindromeInts import PalindromeInts


class TestPalindromeInts(TestCase):

    def test_palindrome(self):
        palindrome_ints = PalindromeInts()
        self.assertEqual(palindrome_ints.is_palindrome_no_str(-121), False)
        self.assertEqual(palindrome_ints.is_palindrome_no_str(1), True)
        self.assertEqual(palindrome_ints.is_palindrome_no_str(22), True)
        self.assertEqual(palindrome_ints.is_palindrome_no_str(121), True)
        self.assertEqual(palindrome_ints.is_palindrome_no_str(10), False)
        self.assertEqual(palindrome_ints.is_palindrome_no_str(101), True)
        self.assertEqual(palindrome_ints.is_palindrome_no_str(122), True)
