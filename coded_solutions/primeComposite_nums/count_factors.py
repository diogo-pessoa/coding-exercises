def solution(N: int) -> int:
    factors = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            factors += 2 if i * i != N else 1
    return factors