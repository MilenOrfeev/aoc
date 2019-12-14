from aoc_utils import load_array
import intcode


def solve():
    program = load_array("input5.txt")
    system_id = 1

    output = intcode.run_program(program, system_id)
    print("Diagnostic code is {}".format(output[-1]))
