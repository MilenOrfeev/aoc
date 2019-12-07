from aoc_utils import load_lines
import task3_1


def populate_locations(moves):
    locations = {}
    current = (0, 0)
    steps = 0

    for move in moves:
        direction = move[0]
        repetitions = int(move[1:])
        for count in range(0, repetitions):
            steps += 1
            current = task3_1.next_location(direction, current)
            locations[current] = steps

    return locations, current


def closest_intersection(first_locations, second_moves):
    centre = (0, 0)
    current = centre
    smallest_delay = -1
    steps = 0

    for move in second_moves:
        direction = move[0]
        repetitions = int(move[1:])
        for count in range(0, repetitions):
            steps += 1
            current = task3_1.next_location(direction, current)
            if current in first_locations:
                delay = steps + first_locations[current]
                if delay < smallest_delay or smallest_delay == -1:
                    smallest_delay = delay

    return smallest_delay


def solve():
    wires = load_lines("input3.txt")
    locations, centre = populate_locations(wires[0].strip().split(','))
    closest = closest_intersection(locations, wires[1].strip().split(','))

    print("Steps from centre to closest intersection is {0}".format(closest))
