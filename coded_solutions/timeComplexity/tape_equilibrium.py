def solution_linear(A):
    total_sum = sum(A)
    left_sum = 0
    minimal_difference = float('inf')  # Initialized to infinity
    for p in range(1, len(A)):
        left_sum += A[p - 1]
        right_sum = total_sum - left_sum
        difference = abs(left_sum - right_sum)  # Absolute difference
        minimal_difference = min(minimal_difference, difference)
    return minimal_difference
