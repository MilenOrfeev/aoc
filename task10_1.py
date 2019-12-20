import math

from aoc_utils import load_lines


def create_graph(lines):
    asteroids = []
    for row_index in range(0, len(lines)):
        for column_index in range(0, len(lines[0])):
            if lines[row_index][column_index] == '#':
                asteroids.append((row_index, column_index))

    return asteroids


def get_visible(station_index, asteroids):
    station = asteroids[station_index]

    asteroids.pop(station_index)
    length = len(set(math.atan2(asteroid[1] - station[1], asteroid[0] - station[0]) for asteroid in asteroids))
    asteroids.insert(station_index, station)

    return length


def find_best_station(asteroids):
    max_visible = 0
    best_station = (0, 0)
    for station_index in range(0, len(asteroids)):
        station = asteroids[station_index]
        visible = get_visible(station_index, asteroids)
        if visible > max_visible:
            max_visible = visible
            best_station = station

    formatted = (best_station[1], best_station[0])
    return max_visible, formatted


def solve():
    asteroids = create_graph(load_lines("input10.txt"))
    max_visible, best_station = find_best_station(asteroids)

    print("The best station is at {} and you can see {} asteroids".format(best_station, max_visible))
