class PalindromeInts:

    @staticmethod
    def is_palindrome(x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        return x == x[::-1]

    @staticmethod
    def is_palindrome_no_str(x: int) -> bool:
        if x and x < 0:
            # If negative, the minus sign breaks palindrome property
            return False
        if x % 10 == 0 and x != 0:
            # If the last digit is 0, the first digit must be 0 (only the number 0
            # satisfies this condition)
            return False

        reversed_num = 0
        original_x = x  # Store the original value of x to compare later

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10

        # The number is a palindrome if it is equal to its reverse or
        # if the reverse without the last digit (in the case of odd number of digits)
        # is equal to the original number divided by 10

        return x == reversed_num or x == reversed_num // 10
