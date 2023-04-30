"""
This program calculates the geometric pattern of a aquare or
rectangle

Project No.Name: 4.8_ Geometric patterns
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def pi_value():
    """
    This function returns the value of PI
    :return: `float`, the value of pi
    """
    return 3.141592653589793


def square_calc(side):
    """
     This function calculates the circumference and area of a
    square
    :param side: `float`, the length of the side
    :return: `float`, circumference and area
    """
    sqr_circumference = (4 * side)
    sqr_area = (side ** 2)
    return sqr_circumference, sqr_area


def rect_calc(side1, side2):
    """
     This function calculates the circumference and area of a
    rectangle
    :param side1: `float`, the length of side 1
    :param side2: `float`, the length of side 2
    :return: `float`, circumference and area
    """
    rect_circumference = (2 * side1) + (2 * side2)
    rect_area = (side1 * side2)
    return rect_circumference, rect_area


def circle_calc(radius):
    """
    This program calculates the circumference and area of a circle
    :param radius: float, the radius of the circle
    :return: float, the circumference and area
    """
    circle_circumference = 2 * pi_value() * radius
    circle_area = pi_value() * (radius ** 2)
    return circle_circumference, circle_area


def print_function(value1, value2):
    """
    This function prints the result
    :return: None
    """
    print(f"The circumference is {value1:.2f}")
    print(f"The surface area is {value2:.2f}")
    print()


def collect_object_data(shape, side):
    """
    This function collects non-zero and non-negative values for a
    required shape of object
    :param shape: `str`, example: circle or square
    :param side: `str`, the name of the side, example: side1 or radius
    :return: `float`, collected data
    """
    value = -1
    prompt = ''

    if shape == "s":
        prompt = f"Enter the length of the square's {side}: "
    elif shape == "r":
        prompt = f"Enter the length of the rectangle's {side}: "
    elif shape == "c":
        prompt = f"Enter the circle's {side}: "

    # this while loop collects data while prevents entering a negative number or zero
    while value < 0 or value == 0:
        value = float(input(prompt))
    return value


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    sqr_side, rect_side1, rect_side2, circle_radius = -1, -1, -1, -1
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")
        allowed_options = ["s", "r", "q", "c"]

        if answer not in allowed_options:
            print("Incorrect entry, try again!")
            print()
        else:
            if answer == "s":
                sqr_side = collect_object_data(answer, "side")
                return answer, sqr_side, None

            elif answer == "r":
                rect_side1 = collect_object_data(answer, "side 1")
                rect_side2 = collect_object_data(answer, "side 2")
                return answer, rect_side1, rect_side2

            elif answer == "c":
                circle_radius = collect_object_data(answer, "radius")
                return answer, circle_radius, None

            else:
                return answer, None, None


def main():
    while True:
        your_choice, value1, value2 = menu()

        if your_choice == "q":
            print("Goodbye!")
            break
        else:
            if your_choice == "s":
                circumference, surface_area = square_calc(value1)
                print_function(circumference, surface_area)
            elif your_choice == "r":
                circumference, surface_area = rect_calc(value1, value2)
                print_function(circumference, surface_area)
            elif your_choice == "c":
                circumference, surface_area = circle_calc(value1)
                print_function(circumference, surface_area)


if __name__ == "__main__":
    main()
