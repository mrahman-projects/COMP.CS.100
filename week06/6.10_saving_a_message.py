"""
This program implements a function that reads inputs entered by the user,
and returns all capitalized form of the given texts

Project No.Name: 6.10_ Saving a Message
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


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


def capitalize_text(text):
    """
    This function capitalize a given list of texts, and returns the list
    :param text: `list`, the input list of text rows
    :return: `list`, all capitalized texts
    """
    text_in_capital = []
    element_in_capital = ""
    for element in text:
        for i in range(len(element)):
            element_in_capital += element[i].upper()
        text_in_capital.append(element_in_capital)
        element_in_capital = ""
    return text_in_capital


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    capitalized_msg = capitalize_text(msg)

    print("The same, shouting:")
    for each_row in capitalized_msg:
        print(each_row)


if __name__ == "__main__":
    main()
