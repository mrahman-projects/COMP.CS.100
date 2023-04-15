"""
This program is an improved version of 2.2.1 and 2.2.2 using
nested loop function

Project No.Name: 2.8.1_Bored? (improved version)
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    bored = False
    while not bored:
        is_bored = input("Bored? (y/n) ").casefold()
        while is_bored == "y":
            print("Well, let's stop this, then.")
            bored = True
            break
        else:
            if is_bored != "n":
                print("Incorrect entry.")


if __name__ == "__main__":
    main()
