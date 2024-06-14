from helpers.TimeItDecorator import timeit_decorator


class LongestSubstringPalindromeManacher:
    def preprocess(self, s: str) -> str:
        # Preprocess the string to add special characters
        return '#' + '#'.join(s) + '#'

    @timeit_decorator
    def longest_palindromic_substring(self, string_input: str) -> str:
        if not string_input:
            return ""

        temporary_string = self.preprocess(string_input)
        length = len(temporary_string)
        list_zeroes = [0] * length
        center = right = 0  # Center and right edge of the rightmost palindrome

        for i in range(length):
            mirror = 2 * center - i  # Mirror of i with respect to center

            if i < right:
                list_zeroes[i] = min(right - i, list_zeroes[mirror])

            # Expand around center i
            while i + list_zeroes[i] + 1 < length and i - list_zeroes[i] - 1 >= 0 and \
                    temporary_string[i + list_zeroes[i] + 1] == temporary_string[
                i - list_zeroes[i] - 1]:
                list_zeroes[i] += 1

            # Update center and right edge
            if i + list_zeroes[i] > right:
                center, right = i, i + list_zeroes[i]

        # Find the maximum element in P
        max_len = max(list_zeroes)
        center_index = list_zeroes.index(max_len)

        # Extract the longest palindromic substring from the original string
        start = (center_index - max_len) // 2
        return string_input[start:start + max_len]
