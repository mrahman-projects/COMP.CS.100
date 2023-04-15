"""
This program asks for input to display the fibonacci series

Project No.Name: 2.7_Fibonacci series
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def main():
    given_number = int(input("How many Fibonacci numbers do you want? "))
    repeat_count = 0
    previous_fib = 1
    current_fib = 1
    # print(previous_fib, current_fib, sep="\n")
    # next_fib = 0
    end_of_series = False

    while not end_of_series:
        repeat_count += 1

        next_fib = previous_fib + current_fib
        print(f"{repeat_count}. {previous_fib}")
        previous_fib = current_fib
        current_fib = next_fib
        if repeat_count == given_number:
            end_of_series = True


if __name__ == "__main__":
    main()
