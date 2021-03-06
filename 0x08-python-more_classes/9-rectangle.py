#!/usr/bin/python3
"""Module for definition of rectangle class.

A module containing a class definition for a printable rectangle.

"""


class Rectangle:
    """A class which creates a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The __init__ method creates a new instance of a Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Returns an informal instance string representation."""
        new_str = ""
        if self.width == 0 or self.height == 0:
            return new_str
        for i in range(self.height - 1):
            new_str = new_str + (str(self.print_symbol) * self.width) + "\n"
        new_str = new_str + str(self.print_symbol) * self.width
        return new_str

    def __repr__(self):
        """Returns an official string representation of an instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the larger rectangle or rect_1 if equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance where heigh == width == size"""
        return cls(size, size)
