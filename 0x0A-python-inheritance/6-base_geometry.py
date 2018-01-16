#!/usr/bin/python3
"""A module which contains an empty class BaseGeometry.


"""


class BaseGeometry:
    """A class which contains the public instance method area() which
       raises an Exception.
    """

    def __init__(self):
        """Initializes an instance of a BaseGeometry object."""
        self.__self = self

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")
