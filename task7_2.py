import itertools
import intcode
import copy

from aoc_utils import load_array


def run_amplifiers(program, sequence):
    amplifiers = []
    for phase in sequence:
        amplifier = copy.deepcopy(program)
        output, inst_pointer = intcode.run_program(amplifier, [phase])
        amplifiers.append((amplifier, inst_pointer))

    output = [0]
    last_from_e = 0
    while len(output) is not 0:
        last_from_e = output[0]

        for a_index in range(0, len(amplifiers)):
            next_amp, inst_pointer = amplifiers[a_index]
            output, inst_pointer = intcode.run_program(next_amp, output, inst_pointer)
            amplifiers[a_index] = (next_amp, inst_pointer)

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
