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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """The getter for the width instance attribute."""
            return self.__width

        @width.setter
        def height(self, value):
            """The setter for the width instance attribute."""
            self.__width = value

        @property
        def height(self):
            """The getter for the height attribute."""
            return self.__height

        @height.setter
        def height(self, value):
            """The setter for the height instance attribute."""
            self.__height = value

        @property
        def x(self):
            """The getter for the x instance attribute."""
            return self.__x

        @x.setter
        def x(self, value):
            """The setter for the x instance attribute."""
            self.__x = value

        @property
        def y(self):
            """The getter for the y instance attribute."""
            return self.__y

        @y.setter
        def y(self, value):
            """The setter for the y instance attribute."""
            self.__y = value
