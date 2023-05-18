"""
This program capitalize the first letter of each word from a given
sentence, and leave rest of the letters at lowercase

Project No.Name: 6.8_ Capitalization
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def capitalize_initial_letters(words):
    """
    This function capitalizes the first letter of each word from a
    given string, and leave the rest of the letter of each word at
    lowercase
    :param words: `str`, the given list of words
    :return: `str`, the transformed list of words
    """
    split_words = words.split()
    transformed_words = ''
    for word in range(len(split_words)):
        first_letter = split_words[word][0].upper()
        transformed_words += first_letter
        for i in range(1, len(split_words[word])):
            transformed_words += split_words[word][i].lower()
        if word < len(split_words)-1:   # to avoid space after the last word
            transformed_words += " "

    return transformed_words


def main():
    given_words = input()
    print(f"{capitalize_initial_letters(given_words)}")


if __name__ == "__main__":
    main()
