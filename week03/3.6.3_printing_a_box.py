"""
This program prints a box as per given instructions

Project No.Name: 3.6.3_ Printing a box
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


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
