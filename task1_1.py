from aoc_utils import load_lines


def fuel_for_mass(mass):
    return mass // 3 - 2


def total_fuel(masses):
    fuels = [fuel_for_mass(mass) for mass in masses]

    return sum(fuels)


def solve():
    lines = load_lines("input1_1.txt")
    masses = [int(x) for x in lines]
    total = total_fuel(masses)

    print("A total of {} fuel will be needed for the modules.".format(total))
