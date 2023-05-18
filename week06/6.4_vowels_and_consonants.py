"""
This program returns total number of vowels and consonants from a
given english word in lower-case letters

Project No.Name: 6.4_ Vowels and Consonants
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def find_in_word(word):
    """
    This function takes a given english word as input and returns the
    total number of vowels and consonants in the word
    :param word: `str`, the given word by the user
    :return: `int`
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count_vowels = 0
    count_consonants = 0
    for i in range(len(word)):
        if word[i] in vowels:
            count_vowels += 1
        else:
            count_consonants += 1
    return count_vowels, count_consonants


def main():
    given_word = input("Enter a word: ")
    if given_word != "":
        total_vowels, total_consonants = find_in_word(given_word)
        print(f'The word "{given_word}" contains {total_vowels} vowels and {total_consonants} consonants.')


if __name__ == "__main__":
    main()
