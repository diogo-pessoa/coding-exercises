from collections import Counter


class LongestSubStrings:

    def __init__(self, s):
        self.s = s

    def sliding_window(self) -> int:
        """
        Len of longest str without repeating chars
        Using a slidingWindow method
        :return: int
        """
        char_list = self.s
        chars_counter = Counter() # could manually build a dict() - using counter instead.
        longest_substring = 0
        left = 0
        right = 0
        while right < len(char_list):
            r_value = char_list[right]
            chars_counter[r_value] += 1 # indexing character by value, and incrementing

            # move left pointer in sliding window, if
            while chars_counter[r_value] > 1:
                l_value = char_list[left]
                chars_counter[l_value] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1) # update

            right += 1


        return longest_substring
