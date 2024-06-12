from unittest import TestCase

from dataStructures.matrix.Matrix import Matrix


class TestMatrix(TestCase):

    def setUp(self):
        print(f"Running test: {self._testMethodName}")
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.matrix = Matrix(data)

    def test__str__matrix(self):
        print(self.matrix)
        self.assertEqual(str(self.matrix), "1 2 3\n4 5 6\n7 8 9")

    def test_print_columns(self):
        self.matrix.print_columns()
        self.assertEqual(self.matrix.print_columns(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_print_single_column(self):
        self.assertEqual(self.matrix.print_columns(1), [2, 5, 8])

    def test_print_single_row(self):
        print(self.matrix.print_row(1))
        self.assertEqual(self.matrix.print_row(1), [4, 5, 6])

    def test_matrix_transpose(self):
        print(self.matrix.transpose())
        self.assertEqual(self.matrix.transpose(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_new_matrix_from_string_rows_by_linebreak(self):
        string_of_elements = "1 2 3\n4 5 6\n7 8 9"
        new_matrix = Matrix.create_matrix_from_string_rows_by_linebreak(
            string_of_elements)
        print(new_matrix)
        self.assertEqual(new_matrix.data, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
