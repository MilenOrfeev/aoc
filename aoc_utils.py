def load_array(text_file):
    with open(text_file) as text:
        line = text.readline()

        numbers = line.strip().split(',')

        return [int(x) for x in numbers]
