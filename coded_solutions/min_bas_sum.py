def solution_1(A: list[int]) -> int:
    """
    val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
    assumption: sum(0) = 0
    For a given array A, we are looking for such a sequence S that minimizes
    val(A,S).
    a = [1, 5, 2, -2] solution_1 -> 0:
    S = [−1, 1, −1, 1], val(A, S) = 0
    n = range(0, 20000)

    :param a: A = [randint(n)] * range(-100,100)
    :returns: val(A, S)
    """
    N = len(A)
    M = sum(abs(a) for a in A)  # Maximum possible sum

    # Convert A to its absolute values as signs are handled by S
    A = [abs(a) for a in A]

    # DP table initialization: dp[sum] checks if sum is achievable
    dp = [False] * (M + 1)
    dp[0] = True  # Zero sum is always achievable

    for a in A:
        next_dp = [False] * (M + 1)
        for s in range(M + 1):
            if dp[s]:
                # If current sum s is achievable, set new sums s + a and
                # |s - a| as achievable
                next_dp[s + a] = True
                next_dp[abs(s - a)] = True
        dp = next_dp

    # The minimum absolute sum achievable is the smallest s where dp[s]
    # is True
    for s in range(M + 1):
        if dp[s]:
            return s


def min_abs_sum(A):
    # Convert A to its absolute values since the signs are to be determined
    A = [abs(a) for a in A]

    # Maximum possible sum of absolute values
    sum_max = sum(A)

    # DP initialization: reachable tells if a specific sum is reachable
    reachable = [False] * (sum_max + 1)
    reachable[0] = True  # Zero is always reachable

    for a in A:
        next_reachable = reachable[:]
        for s in range(sum_max + 1):
            if reachable[s]:
                if s + a <= sum_max:
                    next_reachable[s + a] = True
                if abs(s - a) >= 0:
                    next_reachable[abs(s - a)] = True
        reachable = next_reachable

    # The minimum absolute sum achievable is the smallest s where reachable[
    # s] is True
    for s in range(sum_max + 1):
        if reachable[s]:
            return s
