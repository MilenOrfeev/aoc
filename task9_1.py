from aoc_utils import load_array


def do_operation(instructions, action, par_one, par_two, result_index, input_val, index, relative_base):
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
            index = par_two
    elif action is '6':
        if par_one is 0:
            index = par_two
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
    elif action is '9':
        relative_base += par_one
    else:
        raise ValueError("Invalid action {0}".format(action))

    return index + 1, relative_base


def do_instructions(instructions, input_val):
    index = 0
    relative_base = 0

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
        elif len(command) > 2 and command[-3] == '2':
            par_one = instructions[relative_base + instructions[index]]
        else:
            par_one = instructions[instructions[index]]

        if action not in ('3', '4'):
            index += 1
            if len(command) > 3 and command[-4] == '1':
                par_two = instructions[index]
            elif len(command) > 3 and command[-4] == '2':
                par_two = instructions[relative_base + instructions[index]]
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

        index, relative_base = do_operation(instructions, action, par_one, par_two, result_index, input_val, index, relative_base)


def solve():
    program = load_array("input9.txt")
    program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,9]
    for i in range(0, 10000):
        program.append(0)
    system_id = 1
    do_instructions(program, system_id)
