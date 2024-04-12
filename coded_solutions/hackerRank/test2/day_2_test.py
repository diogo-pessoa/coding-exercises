#!/bin/python3

import os


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    """
    # 2n x 2n matrix of ints

    goal: max the sum of all sub matrices in the upper-left quadrant
    example:

    """
    count_of_rows = len(matrix)
    count_of_cols = len(matrix[0])
    sum = 0
    for i in range(0, count_of_rows // 2):
        for j in range(0, count_of_cols // 2):
            sum += max(matrix[i][j],
                       matrix[i][count_of_cols - j - 1],
                       matrix[count_of_rows - 1 - i][j],
                       matrix[count_of_rows - 1 - i][count_of_cols - 1 - j])
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
