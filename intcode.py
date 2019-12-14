import json


def get_action_info():
    with open('action_data.json', 'r') as data_file:
        data = data_file.read()

    return json.loads(data)


def do_operation(program, data, pr_input, pr_output):
    operation = data['operation']
    if operation == '1':
        program[data['result']] = data['operand1'] + data['operand2']
    elif operation == '2':
        program[data['result']] = data['operand1'] * data['operand2']
    elif operation == '3':
        program[data['result']] = pr_input.pop(0)
    elif operation == '4':
        pr_output.append(data['operand1'])
    elif operation == '5':
        if data['operand1'] != 0:
            data['new_index'] = data['operand2']
    elif operation == '6':
        if data['operand1'] == 0:
            data['new_index'] = data['operand2']
    elif operation == '7':
        if data['operand1'] < data['operand2']:
            program[data['result']] = 1
        else:
            program[data['result']] = 0
    elif operation == '8':
        if data['operand1'] == data['operand2']:
            program[data['result']] = 1
        else:
            program[data['result']] = 0
    else:
        raise ValueError("Invalid action {0}".format(operation))


def prepend_modes(modes, num_ops):
    """Append omitted zeroes to the modes"""
    return modes + ((num_ops - len(modes)) * '0')


def get_operand(program, index, mode):
    if mode is '0':
        return program[program[index]]
    elif mode is '1':
        return program[index]
    else:
        raise ValueError("Invalid mode {0}".format(mode))


def run_program(program, pr_input=None):
    index = 0
    info = get_action_info()
    pr_output = []

    while index < len(program):
        action = str(program[index])

        if action == '99':
            break

        operation = action[-1]
        data = {'operation': operation}
        num_ops = info[action[-1]]['operands']
        modes = prepend_modes(action[:-2][::-1], num_ops)
        for op_count in range(0, num_ops):
            index += 1
            data["operand{}".format(op_count + 1)] = get_operand(program, index, modes[op_count])

        if info[operation]['result']:
            index += 1
            data["result"] = get_operand(program, index, '1')

        data['index'] = index
        do_operation(program, data, pr_input, pr_output)

        if 'new_index' in data:
            index = data['new_index']
        else:
            index += 1

    return pr_output
