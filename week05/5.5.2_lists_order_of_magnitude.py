"""
This program contains a function which checks a list values are in
ascending order or not

Project No.Name: 5.5.2_ A Function for Reviewing a List's Order of
Magnitude
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def is_the_list_in_order(a_list):
    """
    This function check if the list items are in ascending order
    :param a_list: `list`, provided list
    :return: `bool`, True if the list items are in ascending order
    """
    index = 0
    while index < len(a_list):
        if index != len(a_list) - 1:
            if a_list[index] <= a_list[index + 1]:
                index += 1
            else:
                return False
        else:
            return True

    return True


def main():
    print(is_the_list_in_order([37, 40, 40, 43, 45]))


if __name__ == "__main__":
    main()
