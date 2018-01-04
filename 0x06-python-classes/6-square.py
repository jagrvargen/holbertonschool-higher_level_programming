#!/usr/bin/python3


class Square:
    """An empty class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates Square class with a size attribute
        Args:
            size (int): An integer denoting size.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """A getter method which returns the size of the square object."""
        return self.__size

    @size.setter
    def size(self, val):
        """A setter method which sets the value of the size of the object.

        Args:
            val: An integer value denoting size
        """
        self.__size = val
        if type(val) != int:
            print("size must be an integer")
            raise TypeError
        elif val < 0:
            print("size must be >= 0")
            raise ValueError

    @property
    def position(self):
        """A getter method which returns the position coordinates of the square
        """
        return self.__position

    @position.setter
    def position(self, val):
        """A setter method which sets the horizontal and verticak
           positions of the square.

        Args:
            val: A tuple denoting the vertical and horizontal starting points
                 respectively.
        """
        self.__position = val
        if type(val) != tuple:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        elif len(val) != 2 or type(val[0]) != int or type(val[1])  != int:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        elif val[0] < 0 or val[1] < 0:
            print("position must be a tuple of 2 positive integers")
            raise TypeError

    def area(self):
        """A method which returns the area of the Square
        """
        return self.__size * self.__size

    def my_print(self):
        """A method which prints the square using #s
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print(' ')
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(end=' ')
                for k in range(self.size):
                    print('#', end='')
                print()
