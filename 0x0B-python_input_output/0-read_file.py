#!/usr/bin/python3
"""
   This module contains a function which reads and prints a text file.
"""

def read_file(filename=""):
    """Reads a text file (utf-8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            print(line.rstrip())
