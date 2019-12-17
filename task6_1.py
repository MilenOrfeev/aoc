from aoc_utils import load_lines
from collections import defaultdict


def orbits(graph, orbited):
    total_nodes = 0
    total_dependencies = 0
    for orbiting in orbited:
        dependencies,  nodes = orbits(graph, graph[orbiting])
        total_dependencies += dependencies + nodes
        total_nodes += nodes

    return total_dependencies, total_nodes + 1


def solve():
    lines = load_lines('input6.txt')
    graph = defaultdict(list)
    for line in lines:
        orbited, orbiter = line.strip().split(')')
        graph[orbited].append(orbiter)
    print(orbits(graph, graph['COM'])[0])

