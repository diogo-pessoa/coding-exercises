def solution(A: list) -> int:
    """
    This function returns the number of distinct values in a list

    assumptions:
        - N is an integer within the range [0..100,000];
        - each element of array A is an integer within the range [−1,000,
        000..1,000,000].
    :param A:
    :return:
    """
    return len(set(A))
