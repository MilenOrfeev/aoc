
def never_decreases(num_string):
    for index in range(0, len(num_string) - 1):
        left = int(num_string[index])
        right = int(num_string[index + 1])

        if right < left:
            return False

    return True


def has_adjacent_pair(num_string):
    for index in range(0, len(num_string) - 1):
        if num_string[index] == num_string[index + 1]:
            return True
    return False


def solve():
    min_value = 347312
    max_value = 805915

    count = 0
    for number in range(min_value, max_value):
        number_string = str(number)
        if never_decreases(number_string) and has_adjacent_pair(number_string):

            count += 1

    print("There are {0} passwords between {1} and {2}".format(count, min_value, max_value))


