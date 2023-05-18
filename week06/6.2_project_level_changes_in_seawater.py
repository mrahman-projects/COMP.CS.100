"""
This program calculates the level changes in seawater from a given
list of data input by the user. The program displays the results in the
form of Minimum, Maximum, Median, Mean and Standard Deviation of given
data by the user.

Project No.Name: 6.2_ Project: Level Changes in Seawater
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""

from math import sqrt


def user_input():
    """
    This function takes numerical data input from the user.
    The function throws an error if the number of input is less than 2.
    :return: `list`, accumulated user inputs
    """
    given_data = []
    print('Enter seawater levels in centimeters one per line.\n'
          'End by entering an empty line.')

    while True:
        choice = input()
        if choice != "":
            given_data.append(float(choice))  # user inputs are converted into float before entering into the list
        else:
            if len(given_data) < 2:
                print('Error: At least two measurements must be entered!')
                break   # breaks and returns 'None' to 'main'
            else:
                return given_data


def find_minimum(given_list):
    """
    This function returns the minimum value of a given list
    :param given_list: `list`, given list
    :return: `float`, the minimum number
    """
    return min(given_list)


def find_maximum(given_list):
    """
    This function returns the maximum value of a given list
    :param given_list: `list`, given list
    :return: `float`, the maximum number
    """
    return max(given_list)


def find_median(given_list):
    """
    This function returns the minimum value of a given list
    :param given_list: `list`, given list
    :return: `float`, the minimum number
    """
    given_list.sort()  # sorted the list in ascending order
    if len(given_list) % 2 != 0:
        mid_value = int(len(given_list) / 2) + int(len(given_list) % 2)
        return given_list[mid_value - 1]
    else:
        mid_left = int(len(given_list) / 2)
        return (given_list[mid_left - 1] + given_list[mid_left]) / 2


def find_mean(given_list):
    """
    This function returns the mean value of a given list
    :param given_list: `list`, given list
    :return: `float`, the mean value of the given list
    """
    sum_list = 0
    for i in range(len(given_list)):
        sum_list = sum_list + given_list[i]
    return sum_list / len(given_list)


def find_deviation(given_list):
    """
    This function returns the standard deviation of a given list
    :param given_list:`list`, given list
    :return: `float`, the Standard Deviation of the given list
    """
    mean_value = find_mean(given_list)  # collects the mean value from 'find_mean' function
    sum_of_squares = 0
    for i in range(len(given_list)):
        sum_of_squares = sum_of_squares + ((given_list[i] - mean_value) ** 2)
    return sqrt((1 / (len(given_list) - 1)) * sum_of_squares)  # the only place where used the math library for 'sqrt'


def main():
    collected_data = user_input()   # data collection from user

    if collected_data is not None:
        prompt_min = "Minimum:"
        prompt_max = "Maximum:"
        prompt_med = "Median:"
        prompt_mean = "Mean:"
        prompt_dev = "Deviation:"

        print(f"{prompt_min:10} {find_minimum(collected_data):.2f} cm")
        print(f"{prompt_max:10} {find_maximum(collected_data):.2f} cm")
        print(f"{prompt_med:10} {find_median(collected_data):.2f} cm")
        print(f"{prompt_mean:10} {find_mean(collected_data):.2f} cm")
        print(f"{prompt_dev:10} {find_deviation(collected_data):.2f} cm")


if __name__ == "__main__":
    main()
