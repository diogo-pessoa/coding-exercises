# !/bin/python3

import os
import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """
    https://strftime.org/
    time converstion to 2400 format
    params str: hh:mm:ssAM/PM
    returns str: '00:01:00'.
    """
    # converted_format = datetime.datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")

    # print(dt.datetime.fromordinal(s))
    return datetime.datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
