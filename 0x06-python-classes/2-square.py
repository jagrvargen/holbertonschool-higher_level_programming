#!/usr/bin/python3


class Square:
    """An empty class that defines a square"""

    def __init__(self, size=0):
        """Instantiates Square class with a size attribute
        Args:
            size (int): An integer denoting size.
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
