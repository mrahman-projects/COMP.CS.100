"""
This program prints the dates for all the Fridays in 2014

Project No.Name: 2.8.3_TGIF
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    remainder = 7 - 3

    [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec] = \
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for month in range(1, 13):
        if month in [jan, mar, may, jul, aug, octo, dec]:
            end_of_month = 31
            for date in range(7 - remainder, end_of_month + 1, 7):
                print(f"{date}.{month}.")
                remainder = end_of_month - date

        elif month == feb:
            end_of_month = 28
            for date in range(7 - remainder, end_of_month + 1, 7):
                print(f"{date}.{month}.")
                remainder = end_of_month - date

        elif month in [apr, jun, aug, sep, nov]:
            end_of_month = 30
            for date in range(7 - remainder, end_of_month + 1, 7):
                print(f"{date}.{month}.")
                remainder = end_of_month - date


if __name__ == "__main__":
    main()
