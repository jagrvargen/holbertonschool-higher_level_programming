#!/usr/bin/python3
"""
   This module containes a function which appends a string
   to the end of a text file.
"""

def append_write(filename="", text=""):
    """A funtion that appends a string at the end of a text file."""
    with open(filename, mode="a", encoding="utf-8") as fp:
        fp.write(text)
        num_chars = len(text)
    return num_chars
