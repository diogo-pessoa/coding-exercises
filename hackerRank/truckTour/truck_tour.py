def can_complete_tour(petrol: int, distance: int, pumps: int) -> int:
    n = pumps
    total_surplus = 0
    current_surplus = 0
    start_index = 0

    for i in range(n):
        total_surplus += petrol - distance
        current_surplus += petrol - distance

        # If current surplus is negative, reset start index
        if current_surplus < 0:
            start_index = i + 1
            current_surplus = 0

    # If total surplus is negative, it's not possible to complete the circuit
    if total_surplus < 0:
        return -1
    else:
        return start_index


def truck_tour(petrolpumps):
    """
    N petrol pumps in a circle. 0 to N-1.
    info about each pump:
    1. amount of petrol given
    2. distance to the next petrol pump

    Start at any pump
    infinite capacity

    goal

    calculate the first point from where the truck will be able to complete the circle.
    t travel 1 for each liter of petrol
    truck stops on every pump

    ex:
    3
    1 5
    10 3
    3 4

    returns 1

    :param petrolpumps:
    :return:
    """

    n = len(petrolpumps)
    total_surplus = 0
    current_surplus = 0
    start_index = 0

    for i in range(n):
        petrol, distance = petrolpumps[i]
        total_surplus += petrol - distance
        current_surplus += petrol - distance

        # If current surplus is negative, reset start index
        if current_surplus < 0:
            start_index = i + 1
            current_surplus = 0

    # If total surplus is negative, it's not possible to complete the circuit
    if total_surplus < 0:
        return -1
    else:
        return start_index
