import math

from aoc_utils import load_lines


def distance(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def create_graph(lines):
    asteroids = []
    for row_index in range(0, len(lines)):
        for column_index in range(0, len(lines[0])):
            if lines[row_index][column_index] == '#':
                # asteroids.append((row_index, column_index))
                asteroids.append((column_index - 3, row_index - 4))

    return asteroids


def solve():
    asteroids = create_graph(load_lines("input10_test1.txt"))
    centre = (4,3)
    asteroids.remove((0,0))
    asteroids.sort(key=lambda asteroid: math.atan2(asteroid[1], asteroid[0]))
    print(asteroids)
    # lengths = []
    # for station_index in range(0, len(asteroids)):
    #     station = asteroids[station_index]
    #     asteroids.pop(station_index)
    #
    #     x = set(math.atan2(asteroid.y - station.y, asteroid.x - station.x) for asteroid in asteroids)
    #     length = len(set(math.atan2(asteroid.y - station.y, asteroid.x - station.x) for asteroid in asteroids))
    #     lengths.append(length)
    #     asteroids.insert(station_index, station)

    # print("The max asteroids that can be seen is {}".format(max(lengths)))
