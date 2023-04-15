"""
This program is a game called as `Zip Boing`
The first player says 1, the next one 2 and so forth. The game is
called Zip Boing because every time the next number is divisible by 3
the player has to say "zip" and every time the number is divisible by 7
the player has to say "boing". Also, if the umber is divisible by both
the numbers, the player should say "zip boing".

Project No.Name: 2.4.1 Number series game Zip Boing
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    total_numbers = int(input("How many numbers would you like to have?"
                              " "))
    count = 1
    while count <= total_numbers:
        if (count % 3 == 0) and (count % 7 == 0):
            print("zip boing")
        elif count % 3 == 0:
            print("zip")
        elif count % 7 == 0:
            print("boing")
        else:
            print(count)
        count += 1


if __name__ == "__main__":
    main()
