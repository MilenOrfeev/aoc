from aoc_utils import load_comma_arrays


def next_location(direction, current):
    if direction == 'R':
        return current[0], current[1] + 1
    elif direction == 'D':
        return current[0] - 1, current[1]
    elif direction == 'L':
        return current[0], current[1] - 1
    elif direction == 'U':
        return current[0] + 1, current[1]
    else:
        raise ValueError("Invalid Input")


def populate_locations(moves):
    locations = set()
    current = (0, 0)

    for move in moves:
        direction = move[0]
        repetitions = int(move[1:])
        for count in range(0, repetitions):
            current = next_location(direction, current)
            locations.add(current)

    return locations


def closest_intersection(first_locations, second_moves):
    centre = (0, 0)
    current = centre
    smallest_distance = -1

    for move in second_moves:
        direction = move[0]
        repetitions = int(move[1:])
        for count in range(0, repetitions):
            current = next_location(direction, current)
            if current in first_locations:
                current_distance = manhattan_distance(current, centre)
                if current_distance < smallest_distance or smallest_distance == -1:
                    smallest_distance = current_distance

    return smallest_distance


def manhattan_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def solve():
    wires = load_comma_arrays("input3.txt")
    locations = populate_locations(wires[0])
    closest = closest_intersection(locations, wires[1])

    print("Distance from centre to closest intersection is {0}".format(closest))
