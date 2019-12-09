from functools import reduce
from aoc_utils import load_array


def do_operation(instructions, action, parameters, result_index, input_val):
    if action is 1:
        instructions[result_index] = sum(parameters)
    elif action is 2:
        instructions[result_index] = reduce((lambda x, y: x * y), parameters)
    elif action is 3:
        instructions[parameters[0]] = input_val
    elif action is 4:
        print(instructions[parameters[0]])
    else:
        raise ValueError("Invalid action {0}".format(action))


def do_instructions(instructions, input_val):
    index = 0

    while index < len(instructions):
        command = instructions[index]
        print(command)

        if command is 99:
            break

        parameters = []
        action = command
        if action in (1, 2, 3, 4):

            index += 1
            if action in (3, 4):
                parameters.append(instructions[index])
            else:
                parameters.append(instructions[instructions[index]])

            if action in (1, 2):
                index += 1
                parameters.append(instructions[instructions[index]])
        else:
            command = str(command)
            action = int(command[-1])

            for mode in command[:-2][::-1]:
                index += 1
                if mode is '0':
                    parameters.append(instructions[instructions[index]])
                else:
                    parameters.append(instructions[index])

        if action in (1, 2):
            index += 1
            result_index = instructions[index]
        else:
            result_index = -1

        do_operation(instructions, action, parameters, result_index, input_val)
        index += 1


def solve():
    program = load_array("input5.txt")
    system_id = 1
    do_instructions(program, system_id)

