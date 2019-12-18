from aoc_utils import load_array
import intcode


def solve():
    program = load_array("input9.txt")
    # program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    system_id = 1

    output = intcode.run_program(program, [1])
    print(output)

