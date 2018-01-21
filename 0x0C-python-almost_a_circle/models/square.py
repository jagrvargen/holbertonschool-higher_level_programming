#!/usr/bin/python3
"""
   This module ocntains the class definition for Square, which inherits from
   the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class definition. It inherits the x, y, id, width
       and height attributes from the Rectangle class. width and height
       become size in the Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a Square object instance."""
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """
           Overloading method which returns a description of a Square
           instance.
        """
        return "[Square] {} {:d}/{:d} - {:d}".format(self.id, self.x, self.y,\
                                                     self.size)

    @property
    def size(self):
        """The getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """The setter method got the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This method assigns and updates instance attributes."""
        arg_list = ['id', 'size', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, arg_list[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
