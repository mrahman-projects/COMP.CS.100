"""
This program returns a multiplication table where the user choose
a number, and the print continues until the value reached over 100

Project No.Name: 2.3.2_multiplication table, values over a hundred
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    number_to_multiply = int(input("Choose a number: "))
    count = 1

    while True:
        print(str(count) + " * " + str(number_to_multiply) + " = " +
              str(count * number_to_multiply))

        if count * number_to_multiply > 100:
            break

        count += 1


if __name__ == "__main__":
    main()
