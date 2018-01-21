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
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
           Overloading method which returns a description of a Square
           instance.
        """
        return "[Square] {} {:d}/{:d} - {:d}".format(self.id, self.x, self.y,\
                                                     self.size)
