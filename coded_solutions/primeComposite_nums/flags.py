def solution(A: list[int]) -> int:
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
    if len(peaks) < 2:
        return len(peaks)
    for i in range(len(peaks), 0, -1):
        if len(A) % i == 0:
            block_size = len(A) // i
            found = [False] * i
            found_cnt = 0
            for peak in peaks:
                block = peak // block_size
                if not found[block]:
                    found[block] = True
                    found_cnt += 1
            if found_cnt == i:
                return i
    return 0