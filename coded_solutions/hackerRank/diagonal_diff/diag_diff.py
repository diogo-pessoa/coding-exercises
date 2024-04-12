#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diff = 0
    diag_one = []
    diag_two = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                diag_one.append(arr[i][j])
            if i + j == len(arr) - 1:
                diag_two.append(arr[i][j])
    diff = abs(sum(diag_one) - sum(diag_two))
    return diff
# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
