from unittest import TestCase

from leetCode.longestsubstrings.LongestSubStrings import LongestSubStrings


class TestLongestSubStrings(TestCase):
    def test_length_of_longest_substring(self):
        string_val = LongestSubStrings("abcabcbb")
        self.assertEqual(string_val.sliding_window(), 3)
    def test_length_of_longest_substring2(self):
        string_val = LongestSubStrings("bbbbb")
        self.assertEqual(string_val.sliding_window(), 1)
    def test_length_of_longest_substring3(self):
        string_val = LongestSubStrings("pwwkew")
        self.assertEqual(string_val.sliding_window(), 3)

    def test_length_of_longest_substring3(self):
        string_val = LongestSubStrings("pwwkew")
        self.assertEqual(string_val.sliding_window(), 3)

    def test_repeat_chars_in_separate_substrings(self):
        string_val = LongestSubStrings("dvdf")
        self.assertEqual(string_val.sliding_window(), 3)
