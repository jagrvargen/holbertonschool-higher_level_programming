#!/usr/bin/python3
"""
   This module contains a function which reads n number of lines from
   a text file.
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file"""
    with open(filename, encoding="utf-8") as fp:
        if nb_lines <= 0:
            print(fp.read().rstrip())
        else:
            for line in range(nb_lines):
                print(fp.readline().rstrip())
