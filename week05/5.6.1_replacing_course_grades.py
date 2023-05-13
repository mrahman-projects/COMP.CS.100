"""
This program converts any grade > 0 to `6` from a given list of grades
passed as a parameter to the function

Project No.Name: 5.6.1_ Replacing Course Grades
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def convert_grades(list_of_grades):
    """
    This function converts all grade > 0 to '6' (=pass) from a given
    list of grades
    :param list_of_grades:
    :return:
    """
    if len(list_of_grades) > 0:
        for i in range(len(list_of_grades)):
            if list_of_grades[i] > 0:
                list_of_grades[i] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
