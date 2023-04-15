# value = 123
# print(f"1.·»{value}«")
# print(f"2.·»{value:10}«")
# print(f"3.·»{value:>10}«")
# print(f"4.·»{value:<10}«")
# print(f"5.·»{value:^10}«")
# print(f"6.·»{value:2}«")

"""
This program prints a neat table of circle
radii and corresponding circle areas.
"""


def main():
    PI = 3.14159265358979
    FIRST_RADIUS = 1.0
    LAST_RADIUS = 10.0
    STEP = 0.5

    # Column headers
    print("======  ========")
    print("Radius     Area ")
    print("======  ========")

    # Notice how we have to use while loop, since both radii
    # and the step are decimal numbers: range just won't work.

    # Also, a question to ponder: there is something possibly
    # wrong, or at least risky, in the condition of the while loop below.
    # What is it?  Hint: decimal (float) calculations are seldom accurate.

    current_radius = FIRST_RADIUS

    while current_radius <= LAST_RADIUS:
        area = PI * current_radius ** 2

        #   4 wide
        #  1 decimal
        #    ┌─┴─┐
        #   " 6.0    113.097"
        #        └────┬────┘
        #           11 wide
        #          3 decimals

        print(f"{current_radius:4.1f}{area:11.3f}")

        current_radius += STEP


if __name__ == "__main__":
    main()
