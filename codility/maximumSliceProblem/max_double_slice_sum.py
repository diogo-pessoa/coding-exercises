def solution(A: list[int]) -> int:
    n = len(A)

    # Maximum sum slice ending at index (exclusive of the index itself)
    max_ending_here = [0] * n

    # Forward pass for max slice sum excluding the first and last elements
    for i in range(1, n - 1):
        max_ending_here[i] = max(0, max_ending_here[i - 1] + A[i])

    # Maximum sum slice starting at index (exclusive of the index itself)
    max_starting_here = [0] * n

    # Backward pass for max slice sum excluding the first and last elements
    for i in range(n - 2, 0, -1):
        max_starting_here[i] = max(0, max_starting_here[i + 1] + A[i])

    # Find the maximum double slice sum.
    max_double_slice = 0
    for i in range(1, n - 1):
        max_double_slice = max(max_double_slice,
                               max_ending_here[i - 1] + max_starting_here[
                                   i + 1])
    return max_double_slice
