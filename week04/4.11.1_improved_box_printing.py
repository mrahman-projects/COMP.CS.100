"""
This program is the improved version of 'box_print function'
using named parameters

Project No.Name: 4.11.1_Improved Box Printing
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    This function prints a box with inner mark and outer mark
    :param width: `int`, width of the box
    :param height: `int`, height of the box
    :param border_mark: `str`, outside border visual mark
    :param inner_mark: `str`, inside border virual mark
    :return:
    """
    for i in range(height):
        if i == 0:
            print(border_mark * width)
        elif 0 < i < height - 1:
            print(border_mark * 1, end='')
            print(inner_mark * (width - 2), end='')
            print(border_mark * 1)
        elif i == height - 1:
            print(border_mark * width)
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
