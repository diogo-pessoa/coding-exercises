def counting_cars_1(A: list[int]) -> int:
    eastbound_cars = 0  # Count of cars traveling east
    passing_cars = 0  # Count of passing pairs

    for car in A:
        if car == 0:  # Car is traveling east
            eastbound_cars += 1
        else:  # Car is traveling west
            passing_cars += eastbound_cars
    # Check for the condition to avoid large outputs and overflow
    if passing_cars > 1_000_000_000:
        return -1
    return passing_cars


[0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1]