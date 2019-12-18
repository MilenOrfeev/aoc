from aoc_utils import load_array
import intcode


def solve():
    instructions = load_array("input2.txt")

    instructions[1] = 12
    instructions[2] = 2

    intcode.run_program(instructions)

    print("Value at position 0: {}".format(instructions[0]))
