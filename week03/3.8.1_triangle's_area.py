"""
This program demonstrates a function to calculate the area of a
triangle.

Project No.Name: 3.8.1_ Triangle's area
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""
from math import sqrt


def area(first_line, second_line, third_line):
    """
    This function calculates the area of a triangle
    :param first_line: `float`, the length of line 1
    :param second_line: `float`, the length of line 1
    :param third_line: `float`, the length of line 1
    :return: `float`, the area of the triangle
    """
    s = (first_line + second_line + third_line) / 2
    return sqrt(s * (s - first_line) * (s - second_line) * (s - third_line))


def main():
    line_1 = float(input("Enter the length of the first side: "))
    line_2 = float(input("Enter the length of the second side: "))
    line_3 = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is {area(line_1, line_2, line_3):.1f}")


if __name__ == "__main__":
    main()
