def solution(A: list[int]) -> int:
    """
    Assumptions:
        - A slice contains at least two elements.
        - The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... +
        A[Q] / len(slice)
            avg =  (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1)
        - A slice (P, Q) is the same as a slice (P, Q) where P < Q.
        - P i and Q = i+ 1
    Goal:
        - Find the starting position of a slice whose average is minimal.
    Boundaries:
       - returns the starting position of the slice with the minimal average.
        If there is more than one slice with a minimal average,
        return the smallest starting position of such a slice.
       - N is an integer within the range [2..100,000];
       - Each element of array A is an integer within the range [−10,000..10,
       000].
    :param A:
    :return:
    """

    min_avg_value = float('inf')  # Set initial minimum to infinity.
    min_avg_pos = 0  # Initialize the starting position for the minimum
    # average.

    for index in range(0, len(A) - 2):
        # Check the average of the slice of length 2
        avg_2 = (A[index] + A[index + 1]) / 2.0
        if avg_2 < min_avg_value:
            min_avg_value = avg_2
            min_avg_pos = index

        # Check the average of the slice of length 3
        avg_3 = (A[index] + A[index + 1] + A[index + 2]) / 3.0
        if avg_3 < min_avg_value:
            min_avg_value = avg_3
            min_avg_pos = index

    # Check the last two elements
    avg_2 = (A[-2] + A[-1]) / 2.0
    if avg_2 < min_avg_value:
        min_avg_pos = len(A) - 2

    return min_avg_pos
