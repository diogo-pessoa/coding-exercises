def solution(N):
    i = 1
    min_perimeter = 2*(1+N)
    while i*i <= N:
        if N%i == 0:
            min_perimeter = min(min_perimeter, 2*(i+N//i))
        i += 1
    return min_perimeter