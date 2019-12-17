from aoc_utils import load_array
import intcode
import itertools
import copy


def run_amplifiers(program, sequence):
    amp_input = 0
    for phase in sequence:
        copied = copy.deepcopy(program)
        output = intcode.run_program(copied, [phase, amp_input])
        amp_input = output[0]

    return amp_input


def find_best_permutation(program, numbers):
    signals = []
    for permutation in itertools.permutations(numbers):
        signals.append(run_amplifiers(program, permutation))

    return max(signals)


def solve():
    program = load_array('input7.txt')

    max_thruster = find_best_permutation(program, [0, 1, 2, 3, 4])
    print("The highest signal is {}".format(max_thruster))
