from collections import Counter


def solution(A: list[int]) -> int:
    dominator = -1
    unique_elements = set(A)
    for element in unique_elements:
        if A.count(element) > len(A) // 2:
            dominator = element
            break
    return dominator


def solution_with_counter(A: list[int]) -> int:
    counts = Counter(A)
    dominator, count = counts.most_common(1)[0]
    return dominator if count > len(A) // 2 else -1
