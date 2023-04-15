"""
This program implement a program, which only contains a repeating
structure that asks the user's answer again if the answer is not
"y", "Y", "n" or "N".

Project No.Name: 2.2.2_ Bored? (checking for errors)
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    while True:
        # Bored? Answer Y/y or N/n
        answer = input("Answer Y or N: ")
        if answer.casefold() == "y" or answer.casefold() == "n":
            print("You answered " + answer)
            break
        else:
            print("Incorrect entry.")


if __name__ == "__main__":
    main()
