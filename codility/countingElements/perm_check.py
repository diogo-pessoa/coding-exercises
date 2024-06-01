def solution_quadratic(A: list[int]) -> int:
    """
    :param A:
    :return:
    """
    set_of_a = set(range(1, len(A) + 1))
    if sum(set_of_a) - sum(A) == 0:
        return 0
    return 1


def solution_improvement(A: list[int]) -> int:
    """

    :param A:
    :return:
    """
    # exits early if A is empty
    if not A:
        return 0
    set_of_a = set(A)
    # exits early if there are duplicates
    if len(set_of_a) != len(A):
        return 0
    A.sort()  # O(N)
    for i in range(1, len(A) + 1):
        if i != A[i - 1]:
            return 0
    return 1


def solution_improvement_l(A: list[int]) -> int:
    """

    :param A:
    :return:
    """
    # exits early if A is empty
    if not A:
        return 0

    set_of_a = set(A)
    # exits early if there are duplicates
    if len(set_of_a) != len(A):
        return 0
    #  N(N+1)/2
    # target O(Nlog N)
    n = len(A)
    expected_sum = n * ((n + 1) // 2)
    actual_sum = sum(A)
    return 1 if expected_sum == actual_sum else 0
