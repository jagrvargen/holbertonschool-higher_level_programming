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

    def integer_validator(self, name, value):
        """A method which raises exceptions if incorrect types are passed"""
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")


"""A module which contains the class definition for Rectangle.

"""


class Rectangle(BaseGeometry):
    """Class definition for Rectangle object which inherits from
       BaseGeometry class.
    """
    def __init__(self, width, height):
        """Instantiates an instance of a Rectangle object"""
        self.__width = width
        self.__height = height

        self.integer_validator(width, height)
