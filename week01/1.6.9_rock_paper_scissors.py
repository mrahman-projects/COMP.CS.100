"""
This program is a rock/paper/scissor game

Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    player_1_input = input("Player 1, enter your choice (R/P/S): ")
    player_2_input = input("Player 2, enter your choice (R/P/S): ")

    if player_1_input == "R":
        if player_2_input == "P":
            print("Player 2 won!")
        elif player_2_input == "S":
            print("Player 1 won!")
        else:
            print("It's a tie!")

    elif player_1_input == "P":
        if player_2_input == "S":
            print("Player 2 won!")
        elif player_2_input == "R":
            print("Player 1 won!")
        else:
            print("It's a tie!")

    elif player_1_input == "S":
        if player_2_input == "R":
            print("Player 2 won!")
        elif player_2_input == "P":
            print("Player 1 won!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    main()
