"""
This program asks the user to enter 5 numbers, and then prints out
all positive numbers entered through the program

Project No.Name: 5.3.1_ Going Through the Elements of a List
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    numbers = []
    print("Give 5 numbers:")
    for number in range(5):
        numbers.append(int(input("Next number: ")))

    print("The numbers you entered that were greater than zero were:")
    for number in numbers:
        if number > 0:
            print(number)


if __name__ == "__main__":
    main()
