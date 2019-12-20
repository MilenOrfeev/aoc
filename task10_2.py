import math
import task10_1

from collections import OrderedDict
from aoc_utils import load_lines



def distance_from_origin(point):
    return math.sqrt((point[0]) * point[0] + point[1] * point[1])


def create_graph(lines, centre):
    asteroids = []
    for row_index in range(0, len(lines)):
        for column_index in range(0, len(lines[0])):
            if lines[row_index][column_index] == '#':
                if row_index == centre[0] and column_index == centre[1]:
                    continue
                asteroids.append((row_index - centre[0], column_index - centre[1]))

    return asteroids


def format_point(point, centre):
    return point[1] + centre[1], point[0] + centre[0]


def get_destroyed_at(input_filename, destroyed_count):
    asteroids = task10_1.create_graph(load_lines(input_filename))
    max_visible, best_station = task10_1.find_best_station(asteroids)

    centre = (best_station[1], best_station[0])
    asteroids = create_graph(load_lines(input_filename), centre)
    asteroids.sort(key=lambda x: math.atan2(x[1], x[0]), reverse=True)

    buckets = OrderedDict()
    for asteroid in asteroids:
        key = math.atan2(asteroid[1], asteroid[0])
        if key not in buckets:
            value = []
            buckets[key] = value
        else:
            value = buckets[key]
        value.append(asteroid)

    for bucket in buckets.values():
        bucket.sort(key=lambda x: distance_from_origin(x))

    count = 0
    while count < len(asteroids) - 1:
        for key, value in buckets.items():
            if len(value) != 0:
                point = value[0]
                value.pop(0)
                count += 1

                if count == destroyed_count:
                    return format_point(point, centre)


def solve():
    destroyed_count = 200
    destroyed = get_destroyed_at("input10.txt", destroyed_count)
    answer = destroyed[0] * 100 + destroyed[1]

    print("The {}th destroyed asteroid is {}. The puzzle answer is {}".format(destroyed_count, destroyed, answer))



