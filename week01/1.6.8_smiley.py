"""
This program asks the user to rate how they feel in range of 10,
and then the program prints the face expression using `char`

Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    user_feel = int(input("How do you feel? (1-10) "))

    if user_feel == 1:
        print("A suitable smiley would be :'(")
    elif user_feel == 10:
        print("A suitable smiley would be :-D")
    elif 7 < user_feel < 10:
        print("A suitable smiley would be :-)")
    elif 4 <= user_feel <= 7:
        print("A suitable smiley would be :-|")
    elif 1 < user_feel < 4:
        print("A suitable smiley would be :-(")
    else:
        print("Bad input!")


if __name__ == "__main__":
    main()
