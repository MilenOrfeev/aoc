import task4_1


def matches_next(nums, index):
    if index + 1 == len(nums):
        return False
    return nums[index] == nums[index + 1]


def matches_previous(nums, index):
    if index == 0:
        return False
    return nums[index] == nums[index - 1]


def part_of_larger(nums, index):
    return matches_previous(nums, index) or matches_next(nums, index + 1)


def has_adjacent_pair(nums):
    for index in range(0, len(nums) - 1):
        if matches_next(nums, index) and not part_of_larger(nums, index):
            return True
    return False


def solve():
    min_value = 347312
    max_value = 805915

    count = 0
    for number in range(min_value, max_value):
        number_string = str(number)
        if task4_1.never_decreases(number_string) and has_adjacent_pair(number_string):

            count += 1

    print("There are {0} passwords between {1} and {2}".format(count, min_value, max_value))
