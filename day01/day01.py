import math
import sys


def calcModuleFuel(mass):
    return math.floor(mass / 3) - 2


def calcTotalFuel(mass):
    fuel = calcModuleFuel(mass)
    totalFuel = fuel
    fuelFuel = calcModuleFuel(fuel)
    while fuelFuel > 0:
        totalFuel += fuelFuel
        fuelFuel = calcModuleFuel(fuelFuel)

    return totalFuel


def main():
    assert(calcModuleFuel(12) == 2)
    assert(calcModuleFuel(14) == 2)
    assert(calcModuleFuel(1969) == 654)
    assert(calcModuleFuel(100756) == 33583)

    if len(sys.argv) != 2:
        print("Please provide a single input file.")
        exit(1)

    f = open(sys.argv[1], "r")

    totalFuel = 0
    for m in f:
        mass = float(m)
        totalFuel += calcModuleFuel(mass)

    f.close()

    print("Total fuel needed (part 1): " + str(totalFuel))

    assert(calcTotalFuel(14) == 2)
    assert(calcTotalFuel(1969) == 966)
    assert(calcTotalFuel(100756) == 50346)

    f = open(sys.argv[1], "r")

    totalFuel = 0
    for m in f:
        mass = float(m)
        totalFuel += calcTotalFuel(mass)

    f.close()

    print("Total fuel needed (part 2): " + str(totalFuel))


if __name__ == "__main__":
    main()
