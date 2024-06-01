def solution_1(n: int, A: list[int]) -> list[int]:
    """

    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.

    TODO The goal is to calculate the value of every counter after all

    TODO Test for N and M are integers within the range [1..100,000];
    TODO each element of array A is an integer within the range [1..N + 1].
    operations.
    :param A:
    :return:
    """

    if n > 0 and len(A) > 0:
        counters = [0 for _ in range(n)]
        for i in range(len(A)):

            x = A[i]
            current_min = min(counters)
            if 1 <= x <= n:
                counters[x - 1] += 1
            else:
                current_min = max(counters)
        for _ in range(n):
            if counters[_] < current_min:
                counters[_] = current_min
        return counters
    return []


def solution_2(N: int, A: list[int]) -> list[int]:
    if N > 0 and len(A) > 0:
        counters = [0] * N
        current_max = 0
        current_min = 0

        for x in A:
            if 1 <= x <= N:
                # Apply the current_min to the counter if it's behind
                if counters[x - 1] < current_min:
                    counters[x - 1] = current_min

                # Increase the counter by one
                counters[x - 1] += 1

                # Update the current maximum if necessary
                if counters[x - 1] > current_max:
                    current_max = counters[x - 1]
            else:
                # Apply the max counter value to all counters
                current_min = current_max

        # Ensure all counters are at least the last known minimum
        for i in range(N):
            if counters[i] < current_min:
                counters[i] = current_min

        return counters
    return []