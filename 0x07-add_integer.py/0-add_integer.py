#!/usr/bin/python3
"""A module containing an addition function.

   a (int) | (float) : An integer or floating point value.
   b (int) | (float) : AN integer or floating point value.
"""

def add_integer(a, b):
    """
       A function which adds two integers.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
