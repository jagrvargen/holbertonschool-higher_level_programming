#!/usr/bin/python3
"""
   This module contains the class definition for a Rectangle, which
   inherits from the Base class.
"""
from models.base import Base


class Rectangle(Base):
    """This is a class definition for Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a Rectangle object instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter for the width instance attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for the width instance attribute."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for the height instance attribute."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter for the x instance attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for the x instance attribute."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter for the y instance attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for the y instance attribute."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
           A public method which returns the area value of
            the rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
           A public method that prints out the Rectangle instance with
           the # character.
        """
        if (self.y > 0):
            print("\n" * self.y, end="")
        for block in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Returns a string describing Rectangle instance."""
        return "[Rectangle] {} {:d}/{:d} - {:d}/{:d}".format(self.id,\
                            self.x, self.y, self.width, self.height)


    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        arg_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, arg_list[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
