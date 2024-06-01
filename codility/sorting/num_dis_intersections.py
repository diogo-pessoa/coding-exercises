def solution(A: list[int]) -> int:
    # center at i, 0
    # radius is A[i]
    # TODO pending review - missing one intersection
    # discs intersect when j-th and k-th have at least one point in common
    endpoints = []
    for c, radius in enumerate(A):
        endpoints.append((c - radius, 'start'))
        endpoints.append((c + radius, 'end'))

    # Sort by endpoint values; starts come before ends when values
    # are the same
    endpoints.sort(key=lambda x: (x[0], x[1]))

    intersections = 0
    active_disks = 0

    for _, point_type in enumerate(endpoints):
        if point_type == 'start':
            intersections += active_disks
            active_disks += 1
        else:
            active_disks -= 1

        if intersections > 10_000_000:
            return -1
    return intersections
