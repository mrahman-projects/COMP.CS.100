"""
This program asks for the times of the contestant's performances and
prints the result to the hundredth of a second.

Project No.Name: 5.5.3_ Rubik's Cube Solving Contests
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def rubiks_performance():
    """
    This program asks for the times of solving rubik's cube, five times.
    Then removes the lowest and highest times.
    Then returns the average time of solving the challenge using the
    remaining three data.
    :return: `float`, the average of performance
    """
    list_solves = []
    sum_data = 0

    for i in range(1, 5+1):
        list_solves.append(float(input(f"Enter the time for performance {i}: ")))

    list_solves.remove(max(list_solves))
    list_solves.remove(min(list_solves))

    for i in range(len(list_solves)):
        sum_data += list_solves[i]

    return sum_data / len(list_solves)


def main():
    print(f"The official competition score is {rubiks_performance():.2f} seconds.")


if __name__ == "__main__":
    main()
