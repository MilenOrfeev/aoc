from aoc_utils import load_digits
from collections import Counter


def split(items, size):
    return [items[i: i + size] for i in range(0, len(items), size)]


def count_digit(layer, val=0):
    return sum(1 if p == val else 0 for p in layer)


def solve():
    w, h = 25, 6
    digits = load_digits("input5.txt")
    layers = split(digits, w * h)

    best_layer = min(layers, key=lambda l: count_digit(l))

    print(count_digit(best_layer, 1) * count_digit(best_layer, 2))
