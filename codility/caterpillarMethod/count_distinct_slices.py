def solution(M: int, A: list[int]) -> int:
    n = len(A)
    front, back = 0, 0
    distinct_slices = 0
    seen = set()
    while front < n and back < n:
        if A[back] not in seen:
            distinct_slices += back - front + 1
            seen.add(A[back])
            back += 1
        else:
            seen.remove(A[front])
            front += 1
    return min(distinct_slices, 100_000)