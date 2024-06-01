from cffi.backend_ctypes import xrange


def solution_1(A: list[int]) -> int:
    # Find the leader of the array.
    leader = -1
    size = 0
    for i in range(len(A)):
        if size == 0:
            size += 1
            leader = A[i]
        else:
            if A[i] != leader:
                size -= 1
            else:
                size += 1
    count = A.count(leader)
    if count <= len(A) // 2:
        return 0
    equi_leaders = 0
    left_leaders = 0
    for i in range(len(A)):
        if A[i] == leader:
            left_leaders += 1
        if left_leaders > (i + 1) // 2 and count - left_leaders > (
                len(A) - i - 1) // 2:
            equi_leaders += 1
    return equi_leaders


def solution(A: list[int]) -> int:
    leader = max(set(A), key=A.count)
    count = A.count(leader)
    if count <= len(A) // 2:
        return 0
    equi_leaders = sum(1 for i in range(len(A)) if
                       A[i] == leader and count - (i + 1) > (
                               len(A) - i - 1) // 2)
    return equi_leaders


def findLeader(A):
    n = len(A)
    size = 0
    candidate = None

    # First pass: Find the potential candidate.
    for value in A:
        if size == 0:
            candidate = value
            size += 1
        elif value == candidate:
            size += 1
        else:
            size -= 1

    # Second pass: Confirm the candidate is the leader.
    if not candidate:
        return -1  # Early exit if no candidate found

    count = A.count(candidate)

    if count > n // 2:
        return candidate
    else:
        return -1

