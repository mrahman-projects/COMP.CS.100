"""
This program returns the longest substring in alphabetic order inside
a given string

Project No.Name: 6.13_ The Longest Substring in Order
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def longest_substring_in_order(text):
    """
    This function returns the longest substring in order inside a
    given string
    :param text: `str`, the given string
    :return: `str`, the longest substring
    """
    longest_substring_temp = ''
    longest_substring = ''
    counter = 999   # a random number to control a loop

    for i in range(len(text)):
        if i == 0:
            longest_substring_temp += text[0]
            longest_substring = longest_substring_temp
        elif counter == 0:
            longest_substring_temp += text[i]
            counter = 999

        if i < len(text)-1:
            if text[i] < text[i+1]:
                longest_substring_temp += text[i+1]
            else:
                if len(longest_substring_temp) > len(longest_substring):
                    longest_substring = longest_substring_temp
                longest_substring_temp = ''
                counter = 0
        else:
            if len(longest_substring_temp) > len(longest_substring):
                longest_substring = longest_substring_temp
                break

    return longest_substring


def main():
    given_string = input()
    print(f"Longest substring: {longest_substring_in_order(given_string)}")


if __name__ == "__main__":
    main()
