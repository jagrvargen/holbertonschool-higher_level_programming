#!/usr/bin/python3
def print_last_digit(number):
    ### Prints the last digit of a number ###
    if number >= 0:
        print('{:d}'.format(number % 10), end='')
    else:
        number = -number
        print('{:d}'.format(number % 10), end="")
    return (number % 10)