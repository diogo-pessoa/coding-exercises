from unittest import TestCase

from leetCode.palindromicsubstring.LongestSubstringPalindromeManacher import \
    LongestSubstringPalindromeManacher
from leetCode.palindromicsubstring.PalindromicSubString import PalindromicSubstring


class TestPalindromicSubstring(TestCase):

    def setUp(self):
        print(f"Running test: {self._testMethodName}")

    def test_find_longest_palindromic_substring_bb(self):
        substring_palindrome = PalindromicSubstring()
        s = "acacacacac"
        self.assertEqual(substring_palindrome.find_longest_palindromic_substring(s),
                         "acacacaca")

    def test_find_longest_palindromic_substring(self):
        substring_palindrome = PalindromicSubstring()
        s = "acacacacac"
        self.assertEqual(substring_palindrome.find_longest_palindromic_substring(s),
                         "acacacaca")

    def test_find_longest_palindromic_substring_with_manacher_approach(self):
        substring_palindrome = LongestSubstringPalindromeManacher()
        s = "acacac"
        self.assertEqual(substring_palindrome.longest_palindromic_substring(s), "acaca")
