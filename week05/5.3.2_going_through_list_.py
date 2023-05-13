"""
This program first asks the user to enter five numbers, then prints
all numbers in reverse order

Project No.Name: 5.3.2_ Going Through the List Indices
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    numbers = []

    print("Give 5 numbers:")
    for number in range(5):
        numbers.append(int(input("Next number: ")))

    index = len(numbers)
    print("The numbers you entered, in reverse order:")
    while index <= len(numbers):
        print(numbers[index - 1])
        index -= 1
        if index == 0:
            break

    # alternate simple method using for loop
    # for i in range(len(numbers)-1, 0-1, -1):
    #     print(numbers[i])


if __name__ == "__main__":
    main()
