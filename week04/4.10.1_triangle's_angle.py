"""
This program returns the value of a magnitude of an angle

Project No.Name: 4.10.1_ Triangle's angle
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def calculate_angle(a1, a2=90):
    """
    This program contains a function with two functions:
1. Returns the magnitude of the third angle of a triangle, when the
magnitude of two angles are given
2. Returns the magnitude of the other angle, when the magnitude of
one angle is provided of a right-angle
    :param a1: `float`, magnitude of first angle
    :param a2: `float`, magnitude of second angle, if given.
    :return: `float`, magnitude of a third angle if a1, a2 is given,
            else returns other-angle of a right angle
    """
    return 180 - (a1 + a2)


def main():
    calculate_angle(89)


if __name__ == "__main__":
    main()
