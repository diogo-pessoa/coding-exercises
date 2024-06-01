#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def super_digit(n, k):
    """
    Given an integer, we need to find the super digit of the integer.
    If x has only 1 digit, then its super digit is x.
    Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
    :param n:
    :param k:
    :return:
    """
    digit_sum = sum(int(digit) for digit in str(n))
    p = digit_sum * k
    # p = sum([int(x) for x in p])
    if p < 10:
        return p
    else:
        return super_digit(p, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = super_digit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
