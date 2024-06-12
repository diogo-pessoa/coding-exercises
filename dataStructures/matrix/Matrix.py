class Matrix:

    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def __str__(self):
        """
        Break down of output
        using a list comprehension to iterate over each row in the matrix
        and join the elements of each row with a space character
        which is in turn is joined with a newline character
        map() function is used to convert each element in the row to a string

        :return:
        """
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def print_row(self, row_index):
        """

        :return: list of numbers in a row
        """
        if row_index is not None:
            if self.rows <= row_index < 0:
                raise ValueError("Column index out of range")
            return self.data[row_index]

    def print_columns(self, column_index=None):
        """
        Print the all columns of the matrix, unless column is given.

        break-down of output

        first iterate over the columns of the matrix, then iterate over the rows of
        the matrix
        big O - O(n^2) - Need to access every row to get the respective column element
        :param: column_index
        """
        if column_index is not None:
            if column_index >= self.columns or column_index < 0:
                raise ValueError("Column index out of range")
            return [self.data[j][column_index] for j in range(self.rows)]

        return [[self.data[j][i] for j in range(self.rows)] for i in
                range(self.columns)]

    def transpose(self):
        """
        # TODO break down the output
        Transpose the matrix
        What is the definition of a transpose of a matrix?
            The columns of the new matrix are the rows of the original.
        :return: Transposed matrix
        """
        new_matrix = []
        for i in range(self.columns):
            row = []
            for j in range(self.rows):
                row.append(self.data[j][i])
            new_matrix.append(row)
        return new_matrix  # return [[self.data[j][i] for j in range(self.rows)] for
        # i in  #                       range(self.columns)]

    @staticmethod
    def create_matrix_from_string_rows_by_linebreak(string_of_elements):
        """
        Create a matrix from a string of elements separated by a line break
        :param string_of_elements:
        :return: matrix
        """
        data = [[int(i) for i in row.split()] for row in string_of_elements.split('\n')]
        return Matrix(data)
