import intcode
from aoc_utils import load_array


def run_boost(mode):
    program = load_array("input9.txt")
    output = intcode.run_program(program, [mode])
    return output[0]


def solve():
    print("In test mode BOOST outputs {}".format(run_boost(1)))

