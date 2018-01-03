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

    @property
    def size(self):
        """A getter method which returns the size of the square object.
        """
        return self.__size

    @size.setter
    def size(self, val):
        """A setter method which sets the value of the size of the object.

        Args:
            val: An integer value denoting size
        """
        if type(val) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif val < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = val

    def area(self):
        """A method which returns the area of the Square
        """
        return self.__size * self.__size

    def my_print(self):
        """A method which prints the square using #s
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
