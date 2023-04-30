"""
This program can be used to figure out the maximum inflation increase
from the values the user entered. In other words: which is the largest
difference between the consecutive entered values.

Project No.Name: 3.3_Project: Inflation Calculator
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():

    month_count = 1
    prev_inflation = 0.0
    max_inflation_rate = 0.0

    while True:
        curr_inflation = input(f"Enter inflation rate for month {month_count}: ")

        # checking if the user enters the 'Enter' key
        if curr_inflation == "":
            if month_count <= 2:
                print("Error: at least 2 monthly inflation rates must be entered.")
            else:
                print(f"Maximum inflation rate change was {max_inflation_rate:.1f} points.")
            break

        # we need two months data for comparison, so this check
        if month_count > 1:
            curr_inflation_rate = float(curr_inflation) - prev_inflation

            # the first identified inflation rate is always considered as max
            if month_count <= 2:
                max_inflation_rate = curr_inflation_rate

            if curr_inflation_rate > max_inflation_rate:
                max_inflation_rate = curr_inflation_rate

            prev_inflation = float(curr_inflation)
        else:
            prev_inflation = float(curr_inflation)

        month_count += 1


if __name__ == "__main__":
    main()
