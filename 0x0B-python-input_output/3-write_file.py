#!/usr/bin/python3
"""
   This module contains a function which writes an inputted string to
   a text file.
"""


def write_file(filename="", text=""):
    """
       Writes a string to a text file (utf-8) and returns the number of
       characters written.
    """
    with open(filename, mode='w', encoding="utf-8") as fp:
            fp.write(text)
    char_count = len(text)
    return char_count
