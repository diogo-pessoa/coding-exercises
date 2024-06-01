#!/bin/python3

import os


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

# def gridChallenge(grid):

    # sum_ascii = 0
    # for i in range(len(grid)):
    #     if not grid[i].islower():
    #         return "NO"
    #     grid[i] = sorted(grid[i])
    #
    #     for c in grid[i]:
    #         if ord(c) >= sum_ascii - 96:
    #             sum_ascii += ord(c) - 96
    #         else:
    #             return "NO"
    # return "YES"

def gridChallenge(grid):
    sorted_grid = [sorted(row) for row in grid]
    for i in range(len(sorted_grid) - 1):
        for j in range(len(sorted_grid[i])):
            if sorted_grid[i][j] > sorted_grid[i + 1][j]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')
    fptr.close()
