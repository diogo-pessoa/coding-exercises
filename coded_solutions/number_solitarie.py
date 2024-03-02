def solution_ns(A: list[int]) -> int:
    """

    observations:
        - board sequential squares of 0 to n-1, a number on each square
        -  A o len N
        - some squares can be marked during the game (implications?)
        - pebble marks the square
    Goal:
        - The goal of the game is to move the pebble to the last square (N-1)
        - given a non-empty array A of N integers, returns the maximal result
        that can be achieved on the board represented by array A.
    Rules:
        - each turn is a throw of a six-side, k being the face up of the die.
        - the pebble is moved forward k+1 squares, (provided square k+1 exists)
        - k+1 not valid, throw die again, when valid move pebble to k+1(
        marking the square)
        - player score is the sum of k values of marked squares
    Boundaries:
       N is an integer within the range [2..100,000];
       each element of array A is an integer within the range [−10,000..10,000].
    :param A: list of integers representing the board
    :return: int of  sum of player marked squares
    """
    board_size = len(A)
    max_score = [float('-inf')] * board_size  # Initialize DP array with negative infinity.
    max_score[0] = A[0]  # Starting position is known.

    for i in range(1, board_size):
        # Evaluate the maximum reachable score for position i from the last 6
        # positions.
        for die in range(1, 7):
            if i - die >= 0:
                max_score[i] = max(max_score[i], max_score[i - die] + A[i])

    return max_score[board_size - 1]
