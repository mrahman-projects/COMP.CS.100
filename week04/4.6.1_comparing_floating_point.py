"""
This program evaluates the difference of two floating point numbers
with an epsilon value, and returns True of False

Project No.Name: 4.6.1 _ Comparing floating-point (decimal) numbers
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def compare_floats(value1, value2, epsilon_value):
    """
    This function returns `bool` or absolution comparison between two
    float numbers
    :param value1: first `float` value to compare
    :param value2: second `float` value to compare
    :param epsilon_value: given 'float' number to compare
    :return: `bool`
    """
    return abs(value1 - value2) < epsilon_value


def main():
    epsilon = float(input("Provide Epsilon: "))
    v1 = float(input("Provide first value in float: "))
    v2 = float(input("Provide second value in float: "))

    print(compare_floats(v1, v2, epsilon))


if __name__ == "__main__":
    main()
