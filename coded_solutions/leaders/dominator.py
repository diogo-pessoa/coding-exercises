from collections import Counter


def solution(A):
    if not A:
        return -1  # Handle empty array
    counts = Counter(A)
    dominator, count = counts.most_common(1)[
        0]  # Get the most common element and its count

    # Check if the most common element is a dominator
    if count > len(A) // 2:
        return A.index(dominator)  # Return the index of the dominator
    else:
        return -1  # Return -1 if no dominator is found


# def solution(A: list[int]) -> int:
#     dominator = -1
#     unique_elements = set(A)
#     for element in unique_elements:
#         if A.count(element) > len(A) // 2:
#             dominator = element.index()
#             break
#     return dominator


def solution_with_counter(A: list[int]) -> int:
    counts = Counter(A)
    dominator, count = counts.most_common(1)[0]
    return dominator if count > len(A) // 2 else -1
