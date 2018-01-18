#!/usr/bin/python3
"""
   A module which contains an empty class definition for a Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class definition for a Square object which inherits from the Rectangle
       class.
    """

    def __init__(self, size):
        """Instantiates an instance of a Square object."""
        Rectangle.__init__(self, size, size)
        self.__size = size
        self.integer_validator(self, "size", size)
        self.area()

    def __str__(self):
        """Returns a description of a Square object instance."""
        return "[Square] {}/{}".format(self.__size, self.__size)
