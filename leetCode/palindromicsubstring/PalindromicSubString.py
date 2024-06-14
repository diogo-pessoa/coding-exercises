from helpers.TimeItDecorator import timeit_decorator


class PalindromicSubstring:

    def expand_around_center(self, s: str, left: int, right: int) -> str:
        current = s[left + 1:right]
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            current = s[left + 1:right]
        return current or s[left + 1:right]

    @timeit_decorator
    def find_longest_palindromic_substring(self, string_value: str) -> str:
        """
            A palindrome is either odd with a single character: "b"
            Or even with a gap between two chars: "bob"
            # I'm starting with both pointers at zero
        """

        if len(string_value) == 1:
            return string_value
        longest = ""

        left_pointer = 0
        right_pointer = 0
        for i in range(len(string_value)):
            odd_palindrome = self.expand_around_center(string_value, i, i)
            even_palindrome = self.expand_around_center(string_value, i, i + 1)

            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

    def is_palindrome(self, substring) -> bool:
        """
        Useful for storage, but I won't use it on this solution.
        :param substring:
        :return:
        """
        # substring[::-1] - reverses the string
        # string slicing mouthful explanation:
        # slice means "start at the end of the string and end at position 0,
        # move with the step -1" which effectively reverses the string.
        return substring == substring[::-1]
