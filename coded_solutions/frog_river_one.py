def solution(X: int, A: list[int]) -> int:
    """
    This function returns the earliest time when a frog can jump to the other
    side of a river.
    other side of the river X+1
    list(A) is an array of integers representing the falling leaves.
        * A index represents the time when a leaf falls.
        * The Frog can only jump when all the positions from 1 to X are covered
        What's the earliest time when the Array is populated?

    N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
    :param X:
    :param A:
    :return: int the earliest time when the frog can jump to the other side of
    the river
    """
    if A:  # only if A is not empty
        B = [0] * X
        s = 0
        for i in range(0, len(A)):
            if (B[A[i] - 1] == 0) and (A[i] <= X):
                s += 1
                B[A[i] - 1] = 1
            if s == X:
                return i
    return -1


def solution_set(X: int, A: list[int]) -> int:
    """
    This function returns the earliest time when a frog can jump to the other
    side of a river.
    other side of the river X+1
    list(A) is an array of integers representing the falling leaves.
        * A index represents the time when a leaf falls.
        * The Frog can only jump when all the positions from 1 to X are covered
        What's the earliest time when the Array is populated?

    N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
    :param X:
    :param A:
    :return: int the earliest time when the frog can jump to the other side of
    the river
    """
    covered = set()
    for i, leaf in enumerate(A):
        if leaf <= X:
            covered.add(leaf)
        if len(covered) == X:
            return i
    return -1
