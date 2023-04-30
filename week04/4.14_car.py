"""
This program provides depicts a car run by gasoline with limited
fuel capacity and limited mile-age.
It asks the user to fuel the tank, run the car, and quit.
The car does not run more than its mile-age (fuel capacity * mile / liter)

Project No.Name: 4.14_ Car
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    current_gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, current_gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            current_gas = fill(tank_size, to_fill, current_gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            current_gas, x, y = \
                drive(x, y, new_x, new_y, current_gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, current_gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    if to_fill + current_gas <= tank_size:
        return float(to_fill + current_gas)
    else:
        return tank_size


def drive(old_x, old_y, new_x, new_y, current_gas, gas_consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car
    The parameters have to be in this order.

    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    mileage_per_ltr = 100 / gas_consumption
    to_drive = calculate_distance(old_x, old_y, new_x, new_y)

    if enough_gas(to_drive, mileage_per_ltr, current_gas):
        gas_left = current_gas - (to_drive / mileage_per_ltr)
        return gas_left, new_x, new_y
    else:
        allowed_to_drive = current_gas * mileage_per_ltr
        new_x = old_x + calculate_delta_xy(allowed_to_drive, to_drive, new_x, old_x)
        new_y = old_y + calculate_delta_xy(allowed_to_drive, to_drive, new_y, old_y)
        gas_left = 0
        return gas_left, new_x, new_y


def calculate_distance(old_x, old_y, new_x, new_y):
    """
    This function calculates the distance between two x,y coordinates
    :param old_x: `int`, x-point for first x,y coordinate
    :param old_y: `int`, y-point for first x,y coordinate
    :param new_x: `int`, x-point for second x,y coordinate
    :param new_y: `int`, y-point for second x,y coordinate
    :return: `float`, distance between first and second x,y coordinates
    """
    return sqrt(((new_x - old_x) ** 2) + (new_y - old_y) ** 2)


def enough_gas(distance_to_drive, distance_per_ltr, gas_remains):
    """
    This function returns a `bool` if there is enough gas left to
    run a distance
    :param distance_to_drive: `int`, as a km to run
    :param distance_per_ltr: `int`, distance run per litre
    :param gas_remains: `int`, amount of gas left in tank
    :return: `bool`. True if enough gas left
    """
    if gas_remains != 0:
        return distance_to_drive / (distance_per_ltr * gas_remains) <= 1
    else:
        return False


def calculate_delta_xy(can_run, to_run, x2y2, x1y1):
    """
    This function calculates the middle x,y coordinate based on the given
    two x,y coordinate and a given ratio
    :param can_run: `int`, needed to calculate ratio, reflects the car
    actually can run
    :param to_run: `int`, needed to calculate ratio, reflects the car
    wanted to run
    :param x2y2: `int`, the destination x,y coordinate (the car wanted
    to reach to)
    :param x1y1: 'int', the starting x,y point, the car starting from
    :return:
    """
    return (can_run * (x2y2 - x1y1)) / to_run


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
