#!/usr/bin/python3
"""Module for definition of rectangle class.

A module containing a class definition for a printable rectangle.

"""


class Rectangle:
    """A class which creates a rectangle."""

    def __init__(self, width=0, height=0):
        """The __init__ method creates a new instance of a Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width getter returns the value of a Rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter sets the value of a Rectangles's width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height getter returns the height of a Rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter sets the value of a Rectangle's height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A method which returns the width of a Rectangle instance."""
        return self.height * self.width

    def perimeter(self):
        """A method which returns the value of a Rectangle instance's
           perimeter.
        """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return self.height * 2 + self.width * 2
