def solution(A: list[int], B: list[int]) -> int:
    """


    goal:
        to find the number of fish that will stay alive
        given the size of the fish and the direction they are swimming

    assumptions:
        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [0..1,000,000,
        000];
        each element of array B is an integer that can have one of the
        following values: 0, 1;
        the elements of A are all distinct.
    :param A:
    :param B:
    :return:
    """

    stack = []  # Stack to store the sizes of the downstream fish
    surviving_upstream_fish = 0  # Counter for surviving upstream fish

    for i in range(len(A)):
        if B[i] == 1:
            # The fish is swimming downstream, add it to the stack
            stack.append(A[i])
        else:
            # The fish is swimming upstream
            while stack:
                # If there is a fish swimming downstream to compare
                if stack[-1] < A[i]:
                    # The upstream fish eats the downstream fish
                    stack.pop()
                else:
                    # The downstream fish eats the upstream fish,
                    # break the loop
                    break
            else:
                # The stack is empty, meaning this upstream fish survives
                surviving_upstream_fish += 1

    # The total number of surviving fish is the sum of surviving
    # downstream fish
    # (fish remaining in the stack) and all surviving upstream fish
    return len(stack) + surviving_upstream_fish
