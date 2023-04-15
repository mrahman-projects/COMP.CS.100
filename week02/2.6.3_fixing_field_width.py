"""
This program fixes field width from a given program output

Project No.Name: 2.6.3_Fixing field width
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i * j:>4}', end="")
        print()


if __name__ == "__main__":
    main()
