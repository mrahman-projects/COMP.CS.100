"""
This program takes input from users if they are bored.

Project No.Name: 2.2.1 Bored?
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    bored = False
    while not bored:
        is_bored = input("Bored? (y/n) ").casefold()
        if is_bored == "y":
            print("Well, let's stop this, then.")
            bored = True


if __name__ == "__main__":
    main()
