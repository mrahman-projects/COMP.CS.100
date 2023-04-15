"""
This program returns a multiplication table where the user choose
a number

Project No.Name: 2.3.1_multiplication table, school version
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    number_to_multiply = int(input("Choose a number: "))
    count = 1

    while count <= 10:
        # print(str(count) + " * " + str(number_to_multiply) + " = " +
        #       str(count * number_to_multiply))
        print(count, " * ",  number_to_multiply, " = ",
              count * number_to_multiply)
        count += 1


if __name__ == "__main__":
    main()
