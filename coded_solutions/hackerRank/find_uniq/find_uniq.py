#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # sorting the duplicates will show me all duplicates
    value = sorted(a) # constant speed
    repeat = True
    lonely_int = value[-1]
    if len(a) % 2 == 0:
        return 0
    for i in range(0, len(value) -1, 2):
        if value[i] != value[i +1]:
            repeat = False
            lonely_int = value[i]
            break
    return lonely_int

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
