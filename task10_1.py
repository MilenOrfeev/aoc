import math

from aoc_utils import load_lines


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return self.x + " " + self.y


def create_graph(lines):
    asteroids = []
    for row_index in range(0, len(lines)):
        for column_index in range(0, len(lines[0])):
            if lines[row_index][column_index] == '#':
                asteroids.append(Point(row_index, column_index))

    return asteroids


def solve():
    asteroids = create_graph(load_lines("input10.txt"))
    lengths = []
    for station_index in range(0, len(asteroids)):
        station = asteroids[station_index]
        asteroids.pop(station_index)

        length = len(set(math.atan2(asteroid.y - station.y, asteroid.x - station.x) for asteroid in asteroids))
        lengths.append(length)
        asteroids.insert(station_index, station)

    print("The max asteroids that can be seen is {}".format(max(lengths)))
