def load_array(file_name):
    with open(file_name) as text_file:
        line = text_file.readline()

        numbers = line.strip().split(',')

        return [int(x) for x in numbers]


def load_lines(file_name):
    with open(file_name) as text_file:
        return text_file.readlines()


def load_comma_arrays(file_name):
    lines = load_lines(file_name)
    return [line.strip().split(',') for line in lines]

