"""
This program finds out the probability of drawing a combination
of `x` number of balls out of 'y' numbers

Project No.Name: 4.7_Lottery Probabilities
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def factorial(number):
    """
    This function returns the factorial of a given number
    :param number: given number, `int`
    :return: factorial number as `int`
    """
    factorial_of_number = 1
    for i in range(1, number + 1):
        factorial_of_number = factorial_of_number * i
    return factorial_of_number


def combinations(total_number, drawn_number):
    """
    This function determines the total combinations of
    `drawn_number` out of `total_number`
    :param total_number: `int`, is the superset of drawn_number
    :param drawn_number: 'int', is the given smaller set
    from `total_number`
    :return: `int`, the total possibilities
    """
    return int(factorial(total_number) /
               ((factorial(total_number - drawn_number)) *
                factorial(drawn_number)))


def main():
    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))

    if total_balls > 0 and drawn_balls > 0:
        if drawn_balls < total_balls:
            print(f"The probability of guessing all {drawn_balls} balls "
                  f"correctly is "
                  f"1/{combinations(total_balls, drawn_balls)}")
        else:
            print("At most the total number of balls can be drawn.")
    else:
        print("The number of balls must be a positive number.")


if __name__ == "__main__":
    main()
