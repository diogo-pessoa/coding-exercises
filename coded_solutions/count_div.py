def solution_1(a: int, b: int, c: int) -> int:
    range_div = range(a, b+1)
    mod_k = [x % c for x in range_div]
    return mod_k.count(0)
