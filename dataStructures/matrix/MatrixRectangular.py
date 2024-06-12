from dataStructures.matrix.Matrix import Matrix


class RectangularMatrix(Matrix):

    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Matrix is not rectangular")
        super().__init__(data)
