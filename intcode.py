import json


def get_action_info():
    with open('action_data.json', 'r') as data_file:
        data = data_file.read()

    return json.loads(data)


def do_operation(program, data):
    action = data['action']
    if action == '1':
        program[data['result']] = data['operand1'] + data['operand2']
    elif action == '2':
        program[data['result']] = data['operand1'] * data['operand2']
    else:
        raise ValueError("Invalid action {0}".format(action))


def run_program(program):
    index = 0
    info = get_action_info()

    while index < len(program):
        action = str(program[index])

        if action == '99':
            break

        data = {'action': action}
        num_ops = info[action]['operands']
        for op_count in range(1, num_ops + 1):
            index += 1
            data["operand{}".format(op_count)] = program[program[index]]
        if info[action]['result']:
            index += 1
            data["result"] = program[index]

        do_operation(program, data)
        index += 1
