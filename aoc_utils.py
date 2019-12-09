def load_array(file_name):
    with open(file_name) as text_file:
        line = text_file.readline()

        numbers = line.strip().split(',')

        return [int(x) for x in numbers]


def load_lines(file_name):
    with open(file_name) as text_file:
        return text_file.readlines()


def load_digits(file_name):
    with open(file_name) as text_file:
        line = text_file.readline()
        return [int(x) for x in line.strip()]

