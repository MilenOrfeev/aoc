from aoc_utils import load_lines
import task1_1


def calculate_fuel(mass):
    total = 0
    while mass > 0:
        fuel = task1_1.fuel_for_mass(mass)
        total += fuel
        mass = fuel

    return total


def total_fuel(masses):
    fuels = [calculate_fuel(mass) for mass in masses]
    return sum(fuels)


def solve():
    lines = load_lines("input1.txt")
    masses = [int(x) for x in lines]

    total = total_fuel(masses)
    print("A total of {} fuel will be needed".format(total)
          + " for the modules and the fuel itself.")
