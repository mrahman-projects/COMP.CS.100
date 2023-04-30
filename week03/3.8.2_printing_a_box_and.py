"""
This program prints a box with the user provided parameters with the
validation of user inputs, example: a negative value

Project No.Name: 3.8.2_ Printing a box and checking the inputs
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def print_box(width, height, mark):
    """
    This non-returning function prints a box as per given instruction
    :param width: `int`, the width of the box
    :param height: `int`, the height of the box
    :param mark: `str`, the mark to be used
    :return: none
    """
    for i in range(height):
        print(width * mark)


def read_input(prompt):
    """
    This function validates a user given number. It asks for the number
    again in case the number is negative or zero.
    :param prompt: `str`, user provided custom prompt
    :return: `int`, validated positive user input
    """
    while True:
        user_input = int(input(prompt))
        if user_input <= 0:
            continue
        else:
            return user_input


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
