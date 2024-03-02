def solution(A: list[int]) -> int:
    if A:
        max_profit = 0
        min_price = A[0]
        for day in range(1, len(A)):
            min_price = min(min_price, A[day])
            max_profit = max(max_profit, A[day] - min_price)
        return max_profit
    return 0
