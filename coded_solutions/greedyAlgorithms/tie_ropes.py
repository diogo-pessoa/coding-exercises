
def solution(K, A) -> int:
    """

    goal:
    For a given integer K, the goal is to tie the ropes in such a way that the
    number of ropes whose length is greater than or equal to K is maximal.

    Assumptions:
        N is an integer within the range [1..100,000];
        K is an integer within the range [1..1,000,000,000];
        each element of array A is an integer within the range [1..1,000,000,000].
    :param K:
    :param A:
    :return:
    """

    rope_count = 0
    current_length = 0
    for rope in A:
        current_length += rope
        if current_length >= K:
            rope_count += 1
            current_length = 0
    return rope_count
