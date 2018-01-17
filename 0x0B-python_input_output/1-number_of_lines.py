#!/usr/bin/python3


def number_of_lines(filename=""):
    """A function that returns the number of lines of a text file."""
    num_lines = 0
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            num_lines += 1
    return num_lines
