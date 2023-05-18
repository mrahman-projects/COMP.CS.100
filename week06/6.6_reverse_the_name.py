"""
This program reverse a given name in correct order

Project No.Name: 6.6_ Reverse the Names to Correct Order
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def reverse_name(given_string):
    """
    This function corrects the order of a given name
    :param given_string: `str`, the given name
    :return: `str`, the corrected name
    """
    if ',' in given_string:
        split_name = given_string.split(',')
        lastname, firstname = split_name[0].strip(), split_name[1].strip()
        if lastname != '':
            if firstname != '':
                return firstname + ' ' + lastname
            else:
                return lastname
        else:
            return firstname
    else:
        return given_string


def main():
    given_name = input()
    if given_name != "":
        print(f"'{reverse_name(given_name)}'")


if __name__ == "__main__":
    main()
