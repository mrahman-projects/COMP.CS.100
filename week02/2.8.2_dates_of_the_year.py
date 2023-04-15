"""
This program prints all dates of a year which is not a leap-year

Project No.Name: 2.8.2_The dates of the year
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    for month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            for date in range(1, 32):
                print(f"{date}.{month}.")
        elif month == 2:
            for date in range(1, 29):
                print(f"{date}.{month}.")
        elif month in [9, 4, 6, 11]:
            for date in range(1, 31):
                print(f"{date}.{month}.")


if __name__ == "__main__":
    main()
