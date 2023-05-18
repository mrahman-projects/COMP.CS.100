"""
This program forms an acronym by taking the first letter of each
word from the give string

Project No.Name: 6.7_Forming an Acronym
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def create_an_acronym(given_string):
    """
    This function creates an acronym from a given string which should
    contain more than one word
    :param given_string: `str`, the given words
    :return: `str`, the acronym
    """
    if given_string != "":
        split_words = given_string.split()
        acronym = ''
        for word in range(len(split_words)):
            acronym += split_words[word][0].upper()
        return acronym


def main():
    given_words = input()
    print(f"'{create_an_acronym(given_words)}'")


if __name__ == "__main__":
    main()
