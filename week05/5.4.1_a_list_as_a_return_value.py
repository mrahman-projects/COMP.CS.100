"""
This program creates a list of integers, and then finds the occurrence of
 a number from the list and prints that.

Project No.Name: 5.4.1_ A List as a Return Value
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def input_to_list(length_of_list):
    """
    This function read integers from the users, updates the list and
    then return the list
    :param length_of_list: `int`, total length of the list
    :return: `list`, the newly created list
    """
    data_list = []
    print(f"Enter {length_of_list} numbers:")
    for i in range(length_of_list):
        data_list.append(int(input()))

    return data_list


def main():
    number_count = 0
    list_len = int(input("How many numbers do you want to process: "))
    new_list = input_to_list(list_len)

    number_to_search = int(input("Enter the number to be searched: "))
    for number in new_list:
        if number == number_to_search:
            number_count += 1

    if number_count != 0:
        print(f"{number_to_search} shows up {number_count} times among "
              f"the numbers you have entered.")
    else:
        print(f"{number_to_search} is not among the numbers you "
              f"have entered.")


if __name__ == "__main__":
    main()
