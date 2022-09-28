# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Sep. 28, 2022
# This program calculates the cost of a pizza with user defined diameter


import constants


def main():
    diameter = float(input("What is the diameter of your pizza in inches? "))
    print("")
    print(
        "the cost of your pizza is ${:.2f}".format(
            (1.5 * diameter + 4.25) * (constants.HST + 1)
        )
    )


if __name__ == "__main__":
    main()
