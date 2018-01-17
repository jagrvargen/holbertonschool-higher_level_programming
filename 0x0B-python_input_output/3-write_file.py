#!/usr/bin/python3


def write_file(filename="", text=""):
    """
       Writes a string to a text file (utf-8) and returns the number of
       characters written.
    """
    with open(filename, mode='w', encoding="utf-8") as fp:
            fp.write(text)
    char_count = len(text)
    return char_count
