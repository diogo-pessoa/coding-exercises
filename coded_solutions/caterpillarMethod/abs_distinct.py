from cffi.backend_ctypes import xrange


def solution(A):
    return len(set(map(abs, A)))


def caterpillarMethod(A, s):
    n = len(A)
    front, total = 0, 0
    for back in xrange(n):
        while (front < n and total + A[front] <= s): total += A[front]
    front += 1
    if total == s: return True
    total -= A[back]
    return False
