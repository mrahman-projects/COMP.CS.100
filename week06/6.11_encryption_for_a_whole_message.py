"""
This program encrypts the whole multiline given message using the ROT-13
encryption mechanism

Project No.Name: 6.11_ROT-13 Encryption for a Whole Message
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


def row_encryption(row_of_text):
    """
    This function returns a ROT-13 encrypted line of texts
    :param row_of_text: `str`, the given text
    :return: `str`, the encrypted text
    """
    encrypted_text = ''
    for char in range(len(row_of_text)):
        encrypted_text += encrypt(row_of_text[char])
    return encrypted_text


def read_message():
    """
    This function reads from customer input, and saves each row in an
    element of the list
    :return: `list`, the inputs in a list
    """
    list_of_rows = []
    while True:
        each_row = input()
        if each_row == "":
            break
        else:
            list_of_rows.append(each_row)

    return list_of_rows


def main():

    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for each_row in msg:
        encrypted_message = row_encryption(each_row)
        print(encrypted_message)


if __name__ == "__main__":
    main()
