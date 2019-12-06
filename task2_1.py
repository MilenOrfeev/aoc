from aoc_utils import load_array


class Operation:
    pass


def do_operation(instructions, operation):
    if operation.action == 1:
        instructions[operation.result_index] = operation.left_operand + operation.right_operand
    else:
        instructions[operation.result_index] = operation.left_operand * operation.right_operand


def do_instructions(instructions):
    index = 0

    while index < len(instructions):
        action = instructions[index]

        if action == 99:
            break

        operation = Operation()
        operation.action = action
        operation.left_operand = instructions[instructions[index + 1]]
        operation.right_operand = instructions[instructions[index + 2]]
        operation.result_index = instructions[index + 3]

        do_operation(instructions, operation)

        index += 4


def solve():
    instructions = load_array("input2_1.txt")
    instructions[1] = 12
    instructions[2] = 2

    do_instructions(instructions)

    print(instructions[0])
