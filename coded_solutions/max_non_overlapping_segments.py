def solution(A: list[int], B: list[int]) -> int:
    """
    goal:
    The goal is to find the maximal number of non-overlapping segments.
    Assumptions:
        N is an integer within the range [0..30,000];
        each element of arrays A, B is an integer within the range [0..1,000,
        000,000];
        A[i] ≤ B[i], for each i (0 ≤ i < N);
        B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).
    :param A:
    :param B:
    :return:
    """

    count = 0  # Counter for maximum non-overlapping segments
    last_end = -1  # Variable to track the end of the last chosen segment

    for i in range(len(A)):
        # If the current segment does not overlap with the last chosen one
        if A[i] > last_end:
            count += 1  # Increment the count
            last_end = B[i]  # Update the end point

    return count

