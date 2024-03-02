def solution_bad_time_complexity(a: int, b: int, c: int) -> int:
    range_div = range(a, b+1)
    mod_k = [x % c for x in range_div]
    return mod_k.count(0)

def solution_1(x: int, y: int, K: int) -> int:
    if x % K == 0:
        first_divisible = x
    else:
        first_divisible = x + (K - x % K)
    last_divisible = y - y % K

    if first_divisible > y:
        return 0

    return (last_divisible - first_divisible) // K + 1
