"""
This program creates a function to check if the lists members have
equal values

Project No.Name: 5.5.2 _ A Function for Comparing Whether List Members
Have an Equal Value
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def are_all_members_same(a_list):
    """
    This function checks whether all elements of a list are same or not
    :param a_list: `list`, provided list
    :return: `bool`, True if the values are same
    """
    index = 0
    while index < len(a_list):
        if index != len(a_list) - 1:
            if a_list[0] != a_list[index + 1]:
                return False
        index += 1

    else:
        return True

    # alternate simple method

    # if len(a_list) > 0:
    #     if max(a_list) == min(a_list):
    #         return True
    #     else:
    #         return False
    # else:
    #     return True


def main():
    print(are_all_members_same([42, 42, 42, 43]))


if __name__ == "__main__":
    main()
