#!/usr/bin/python3


def append_write(filename="", text=""):
    """A funtion that appends a string at the end of a text file."""
    with open(filename, mode="a", encoding="utf-8") as fp:
        fp.write(text)
        num_chars = len(text)
    return num_chars
