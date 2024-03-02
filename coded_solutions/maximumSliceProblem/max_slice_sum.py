def solution(A):
    """
    Uses the Kadane's algorithm to find the maximum
    sum of any subarray. We keep track of the maximum sum ending at the
    current position (max_ending) and the maximum sum of any subarray seen so
    far (max_slice). The maximum sum of any subarray is then returned.
    :param A:
    :return:
    """
    max_ending = max_slice = A[0]
    for a in A[1:]:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice
