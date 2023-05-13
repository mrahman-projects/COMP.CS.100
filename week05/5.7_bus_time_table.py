"""
This program prints three bus schedules from a list of schedule, when
the user delivers a time to check

Project No.Name: 5.7_Bus Time Table
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    bus_schedules = [630, 1015, 1415, 1620, 1720, 2000]
    next_schedules = []
    time_of_choice = int(input("Enter the time (as an integer): "))

    for i in range(len(bus_schedules)):
        if time_of_choice <= bus_schedules[i]:
            if i < len(bus_schedules) - 3:
                for each in range(i, i+3):
                    next_schedules.append(bus_schedules[each])
                break
            else:
                borrow_from_begin = 3 - (len(bus_schedules) - i)
                for each in range(i, len(bus_schedules)):
                    next_schedules.append(bus_schedules[each])
                for each in range(borrow_from_begin):
                    next_schedules.append(bus_schedules[each])
                break
        elif time_of_choice > bus_schedules[len(bus_schedules) - 1]:
            for each in range(3):
                next_schedules.append(bus_schedules[each])
            break

    print("The next buses leave:")
    for each in next_schedules:
        print(each)


if __name__ == "__main__":
    main()
