"""
This program creates functions to print the words for Old MacDonald
Had a Farm

Project No.Name: 3.6.1_The song "Old MacDonald had a farm"
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def print_verse(animal, vocal):
    """
    This function takes input from main program to print non-returned
    rhymes paragraph
    :param animal: `str`, the animal name
    :param vocal: 'str', the animal makes sound with
    :return: None
    """
    print("Old MACDONALD had a farm\nE-I-E-I-O")
    print(f"And on his farm he had a {animal}\nE-I-E-I-O")
    print(f"With a {vocal} {vocal} here")
    print(f"And a {vocal} {vocal} there")
    print(f"Here a {vocal}, there a {vocal}")
    print(f"Everywhere a {vocal} {vocal}")
    print("Old MacDonald had a farm\nE-I-E-I-O")


def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
