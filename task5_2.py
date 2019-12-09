from aoc_utils import load_array


def do_operation(instructions, action, par_one, par_two, result_index, input_val, index):
    if action is '1':
        instructions[result_index] = par_one + par_two
    elif action is '2':
        instructions[result_index] = par_one * par_two
    elif action is '3':
        instructions[par_one] = input_val
    elif action is '4':
        print(par_one)
    elif action is '5':
        if par_one is not 0:
            return par_two
    elif action is '6':
        if par_one is 0:
            return par_two
    elif action is '7':
        if par_one < par_two:
            instructions[result_index] = 1
        else:
            instructions[result_index] = 0
    elif action is '8':
        if par_one == par_two:
            instructions[result_index] = 1
        else:
            instructions[result_index] = 0
    else:
        raise ValueError("Invalid action {0}".format(action))

    return index + 1


def do_instructions(instructions, input_val):
    index = 0

    while index < len(instructions):
        command = instructions[index]

        if command is 99:
            break

        command = str(command)
        action = command[-1]

        index += 1
        if action is '3':
            par_one = instructions[index]
        elif len(command) > 2 and command[-3] == '1':
            par_one = instructions[index]
        else:
            par_one = instructions[instructions[index]]

        if action not in ('3', '4'):
            index += 1
            if len(command) > 3 and command[-4] == '1':
                par_two = instructions[index]
            else:
                par_two = instructions[instructions[index]]

            if action not in ('5', '6'):
                index += 1
                result_index = instructions[index]
            else:
                result_index = -1
        else:
            par_two = -1
            result_index = -1

        index = do_operation(instructions, action, par_one, par_two, result_index, input_val, index)


def solve():
    program = load_array("input5.txt")
    system_id = 5
    do_instructions(program, system_id)
