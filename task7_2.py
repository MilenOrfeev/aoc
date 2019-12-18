import itertools
import copy

from aoc_utils import load_array
from intcode import Intcode


def run_amplifiers(program, sequence):
    amplifiers = []
    for phase in sequence:
        code = copy.deepcopy(program)
        amplifier = Intcode(code, [phase])
        amplifier.run()
        amplifiers.append(amplifier)

    output = [0]
    last_from_e = 0
    while len(output) is not 0:
        last_from_e = output[0]

        for index in range(0, len(amplifiers)):
            amplifier = amplifiers[index]
            if len(output) > 0:
                amplifier.add_input(output[0])
            output = amplifier.run()

    return last_from_e


def find_best_permutation(program, numbers):
    signals = []
    for permutation in itertools.permutations(numbers):
        signals.append(run_amplifiers(program, permutation))

    return max(signals)


def solve():
    program = load_array("input7.txt")
    max_thruster = find_best_permutation(program, [5, 6, 7, 8, 9])

    print("The highest signal is {}".format(max_thruster))
