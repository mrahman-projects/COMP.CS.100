"""
This program returns the number of 'abba's in a overlapping given string

Project No.Name: 6.12_ How Many abbas?
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def count_abbas(text):
    """
    This function returns the repeat count of the text 'abba' from
    the given text
    :param text: `str`, the given input of text
    :return: `int`
    """
    count = 0
    for i in range(len(text)):
        if text[i] == 'a':
            if text[i+1:i+4] == 'bba':
                count += 1

    return count


def main():

    given_string = input()
    print(f'Count of "abba": {count_abbas(given_string)}')


if __name__ == "__main__":
    main()
