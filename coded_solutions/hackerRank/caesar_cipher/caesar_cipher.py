#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encrypted_string = []
    for c in s:
        current_letter = c
        skip = k
        if c.isalpha():
            pass
             # Base order from first letter in alphabet
            base = ord('A') if c.isupper() else ord('a')
            char_pos = ord(c) - base

            # Calculate new position using modular arithmetic for wrap-around
            # # Calculate based on ASCII Table if Upper /lower base is
            new_pos = (char_pos + skip) % 26
        # TODO convert back to char
            new_char = chr(base + new_pos)
        # TODO append to encrypted_string
            encrypted_string.append(new_char)
        else:
            encrypted_string.append(c)
    return ''.join(encrypted_string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
