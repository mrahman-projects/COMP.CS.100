"""
This program demonstrates functions usability inside another function
using the song "Yogi Bear"

Project No.Name: 3.6.2_ The song "Yogi Bear"
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def repeat_name(name, repeat_count):
    """
    This function prints a bear name in a specific order with given
    number of count
    :param name: `str`, the bear name
    :param repeat_count: `int`, the repeat of the name
    :return: None
    """
    for i in range(repeat_count):
        print(f"{name}, {name} Bear")


def verse(determinator, name):
    """
    this function prints the main body of the rhymes by using the given
    verses
    :param determinator: `str`, the first line of the paragraph
    :param name: `str`, the bear name
    :return: none
    """
    print(f"{determinator}")
    print(f"{name}, {name}")
    print(f"{determinator}")
    repeat_name(name, 3)
    print(f"{determinator}")
    repeat_name(name, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
