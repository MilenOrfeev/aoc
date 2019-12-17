from aoc_utils import load_lines
from collections import defaultdict


def min_transfers(graph):
    star_moves = {}

    you = 'YOU'
    my_count = 0
    while you != 'COM':
        # You move up
        star_moves[graph[you]] = my_count
        you = graph[you]
        my_count += 1

    # Santa moves up until he reaches me
    santa_count = 0
    santa = graph['SAN']
    while santa not in star_moves:
        santa_count += 1
        santa = graph[santa]

    return santa_count + star_moves[santa]


def solve():
    lines = load_lines('input6.txt')
    graph = {}
    for line in lines:
        orbited, orbiter = line.strip().split(')')
        graph[orbiter] = orbited

    print(min_transfers(graph))

