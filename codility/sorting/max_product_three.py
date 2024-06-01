def solution(A) -> int:
    """
    goal:
    Given an array A, the goal is to find the maximal product of any triplet.
    Assumptions:
        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
    :param A:
    :return:
    """
    A.sort()
    # A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
    #  multiplying the first two elements of array, since they could be negative values,
    # yelding a positive higher than the largest values at the end of sorted array
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])