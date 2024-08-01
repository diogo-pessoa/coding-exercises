import math


class ZigZagConversion:

    @staticmethod
    def zig_zag_the_string(s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        # TODO - really complicated way of find the columns
        len_of_zigzag_string = len(s)
        sections = math.ceil(len_of_zigzag_string / (2 * num_rows - 2.0))
        num_cols = sections * (num_rows - 1)

        matrix = [[""] * num_cols for _ in range(num_rows)]

        curr_row, curr_col = 0, 0
        curr_string_index = 0

        # Iterate in zig-zag pattern on matrix and fill it with string characters.
        while curr_string_index < len_of_zigzag_string:
            # Move down.
            while curr_row < num_rows and curr_string_index < len_of_zigzag_string:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            curr_row -= 2
            curr_col += 1

            # Move up (with moving right also).
            while (curr_row > 0 and curr_col < num_cols and curr_string_index < len_of_zigzag_string):
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1

        answer = ""
        for row in matrix:
            answer += "".join(row)

        return answer.replace(" ", "")
