import copy
import json


class Intcode(object):
    """The Intcode computer that is used in The Advent Of Code

    Attributes:
        program: Program that is being run on the computer.
        pr_input: An array with the initial input to the program.
        index: Current value of the instruction pointer
    """

    def __init__(self, program, pr_input):
        self.program = program
        self._pr_input = copy.deepcopy(pr_input)
        self.index = 0
        self._pr_output = []
        self.info = Intcode.get_action_info()

    @staticmethod
    def get_action_info():
        with open('action_data.json', 'r') as data_file:
            data = data_file.read()

        return json.loads(data)

    @staticmethod
    def _prepend_modes(modes, num_ops):
        """Append omitted zeroes to the modes"""
        return modes + ((num_ops - len(modes)) * '0')

    def do_operation(self, data):
        program = self.program
        operation = data['operation']
        if operation == '1':
            program[data['result']] = data['operand1'] + data['operand2']
        elif operation == '2':
            program[data['result']] = data['operand1'] * data['operand2']
        elif operation == '3':
            program[data['result']] = self._pr_input.pop(0)
        elif operation == '4':
            self._pr_output.append(data['operand1'])
        elif operation == '5':
            if data['operand1'] != 0:
                self.index = data['operand2']
        elif operation == '6':
            if data['operand1'] == 0:
                self.index = data['operand2']
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

    def get_operand(self, mode):
        program = self.program
        if mode is '0':
            return program[program[self.index]]
        elif mode is '1':
            return program[self.index]
        else:
            raise ValueError("Invalid mode {0}".format(mode))

    def get_operation_data(self, action):
        operation = action[-1]
        data = {'operation': operation}

        num_ops = self.info[action[-1]]['operands']
        modes = Intcode._prepend_modes(action[:-2][::-1], num_ops)
        for op_count in range(0, num_ops):
            self.index += 1
            data["operand{}".format(op_count + 1)] = self.get_operand(modes[op_count])

        if self.info[operation]['result']:
            self.index += 1
            data["result"] = self.get_operand('1')

        return data

    def run_program(self):
        program = self.program
        pr_output = []

        while self.index < len(program):
            action = str(program[self.index])

            if action == '99':
                break

            operation = action[-1]
            if operation == '3' and len(self._pr_input) == 0:
                # Freeze program
                break

            op_data = self.get_operation_data(action)
            self.do_operation(op_data)

        output_so_far = copy.deepcopy(pr_output)
        self._pr_output = []
        return output_so_far
