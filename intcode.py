import copy
import json


class Memory(object):
    def __init__(self, code):
        self._memory = code
        self._memory.extend([0] * len(code))

    def write(self, index, element):
        self.extend_if_needed(index)
        self._memory[index] = element

    def read(self, index):
        self.extend_if_needed(index)
        return self._memory[index]

    def extend_if_needed(self, index):
        while index > len(self._memory):
            new_length = int(len(self._memory) * 1.5)
            self._memory.extend([0] * new_length)

    def read_all(self):
        return copy.deepcopy(self._memory)

    def get_length(self):
        return len(self._memory)


class Intcode(object):
    """The Intcode computer that is used in The Advent Of Code

    Attributes:
        program: Program that is being run on the computer.
        pr_input: An array with the initial input to the program.
        index: Current value of the instruction pointer
    """

    def __init__(self, program, pr_input):
        self.memory = Memory(program)
        self._pr_input = copy.deepcopy(pr_input)
        self.index = 0
        self._pr_output = []
        self.info = Intcode.get_action_info()
        self.relative_base = 0

    @staticmethod
    def get_action_info():
        with open('action_data.json', 'r') as data_file:
            data = data_file.read()

        return json.loads(data)

    @staticmethod
    def _prepend_modes(modes, num_ops):
        """Append omitted zeroes to the modes"""
        return modes + ((num_ops - len(modes)) * '0')

    def add_input(self, value):
        self._pr_input.append(value)

    def do_operation(self, data):
        self.index += 1

        memory = self.memory
        operation = data['operation']
        if operation == '1':
            memory.write(data['result'],  data['operand1'] + data['operand2'])
        elif operation == '2':
            memory.write(data['result'], data['operand1'] * data['operand2'])
        elif operation == '3':
            memory.write(data['result'], self._pr_input.pop(0))
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
                memory.write(data['result'], 1)
            else:
                memory.write(data['result'], 0)
        elif operation == '8':
            if data['operand1'] == data['operand2']:
                memory.write(data['result'], 1)
            else:
                memory.write(data['result'], 0)
        elif operation == '9':
            self.relative_base += data['operand1']
        else:
            raise ValueError("Invalid action {0}".format(operation))

    def get_operand(self, mode):
        memory = self.memory
        if mode is '0':
            return memory.read(memory.read(self.index))
        elif mode is '1':
            return memory.read(self.index)
        elif mode is '2':
            address = self.relative_base + memory.read(self.index)
            return memory.read(address)
        else:
            raise ValueError("Invalid mode {0}".format(mode))

    def get_operation_data(self, action):
        operation = action[-1]
        data = {'operation': operation}

        num_ops = self.info[action[-1]]['operands']
        modes = Intcode._prepend_modes(action[:-2][::-1], num_ops + 1)
        for op_count in range(0, num_ops):
            self.index += 1
            data["operand{}".format(op_count + 1)] = self.get_operand(modes[op_count])

        if self.info[operation]['result']:
            self.index += 1
            if modes[-1] == '2':
                address= self.relative_base + self.memory.read(self.index)
                data['result'] = address
            else:
                data["result"] = self.get_operand('1')

        return data

    def run(self):
        memory = self.memory

        while self.index < memory.get_length():
            action = str(memory.read(self.index))

            if action == '99':
                break

            operation = action[-1]
            if operation == '3' and len(self._pr_input) == 0:
                # Freeze program
                break

            op_data = self.get_operation_data(action)
            self.do_operation(op_data)

        output_so_far = copy.deepcopy(self._pr_output)
        self._pr_output = []
        return output_so_far


def run_program(program, pr_input=None):
    if pr_input is None:
        pr_input = []
    intcode = Intcode(program, pr_input)
    return intcode.run()

