"""
This program practices a print command separator character

Project No.Name: 2.6.2_Fixing the spaces
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    your_name = input("Tell us your name: ") + ','
    print("Hey", your_name, "the printout formatting is going well!", sep=" ")


if __name__ == "__main__":
    main()
