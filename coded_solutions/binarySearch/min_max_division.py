def check_blocks(K: int, max_block_sum: int, A: list[int]) -> int:
    block_count = 1
    current_block_sum = 0
    for a in A:
        if current_block_sum + a > max_block_sum:
            block_count += 1
            current_block_sum = a
            if block_count > K:
                return False
        else:
            current_block_sum += a
    return True


def optimal_large_sum(A, K):
    lower_bound = max(A)  # No block sum can be less than the largest element.
    upper_bound = sum(
        A)  # No block sum can be more than the sum of all elements.
    result = 0
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if check_blocks(A, mid, K):
            result = mid
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return result


def check_blocks(K: int, max_block_sum: int, A: list[int]) -> int:
    block_count = 1
    current_block_sum = 0
    for a in A:
        if current_block_sum + a > max_block_sum:
            block_count += 1
            current_block_sum = a
            if block_count > K:
                return False
        else:
            current_block_sum += a
    return True


def solution(K: int, M: int, A: list[int]) -> int:
    lower_bound = max(A)
    upper_bound = sum(A)
    result = 0
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if check_blocks(K, mid, A):
            result = mid
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return result
