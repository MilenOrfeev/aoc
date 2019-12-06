import copy
import task2_1
from aoc_utils import load_array


def noun_verb_pair(instructions, desired, highest):
    for noun in range(0, highest):
        for verb in range(0, highest):
            copied = copy.deepcopy(instructions)
            copied[1] = noun
            copied[2] = verb
            task2_1.do_instructions(copied)

            if copied[0] == desired:
                return noun, verb

    raise ValueError("Wrong input")


def solve():
    instructions = load_array("input2_1.txt")
    noun, verb = noun_verb_pair(instructions, desired=19690720, highest=99)

    print("Found noun {0} and verb {1}".format(noun, verb))
    print("100 * noun + verb = {0}".format(100 * noun + verb))



