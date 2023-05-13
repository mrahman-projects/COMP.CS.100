"""
This program prints even numbers from 0 to 100 in an ascending order,
and then in descending order

Project No.Name: 5.2_Number Sequences
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    for number in range(0, 100 + 1, 2):
        print(number)

    for number in range(100, 0 - 1, -2):
        print(number)


if __name__ == "__main__":
    main()
