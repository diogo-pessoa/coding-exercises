def solution_1(A: list[int]) -> int:
    if A:
        filtered_A = [a for a in A if a > 0]

        # Convert the filtered list to a set.
        num_set = set(filtered_A)

        # Iterate from 1 to len(A) + 1 to find the smallest missing integer.
        for i in range(1, len(A) + 2):
            if i not in num_set:
                return i
    return 1