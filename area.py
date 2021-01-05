#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program uses user defined functions to calculate the area of a triangle


def calculate_area(length, width):
    # calculate area

    # process
    area = length * width / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets length and width

    # input
    try:
        base_from_user = int(input("Enter the base "
                                   "length of a triangle (cm): "))
        height_from_user = int(input("Enter the height of a triangle (cm): "))
        print("")

        # call functions
        calculate_area(base_from_user, height_from_user)
    except ValueError:
        print("")
        print("That cannot be calculated because you entered an invalid key.")


if __name__ == "__main__":
    main()
