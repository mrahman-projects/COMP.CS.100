"""
This program encrypts a given string using the ROT-13 encryption
formula

Project No.Name: 6.9_ ROT-13 Encryption of One Line
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text.lower() in regular_chars:
        after_encrypt = encrypted_chars[regular_chars.index(text.lower())]
        if text.isupper():
            return after_encrypt.upper()
    else:
        return text

    return after_encrypt


def row_encryption(text):
    """
    This function returns a ROT-13 encrypted line of texts
    :param text: `str`, the given text
    :return: `str`, the encrypted text
    """
    encrypted_text = ''
    for char in range(len(text)):
        encrypted_text += encrypt(text[char])
    return encrypted_text


def main():
    given_string = input()
    print(f"{row_encryption(given_string)}")


if __name__ == "__main__":
    main()
