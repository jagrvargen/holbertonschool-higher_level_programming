#!/usr/bin/python3
"""A module containing the class definition MyList.


"""


class MyList(list):
    """A class which inherits from list object."""

    def __init__(self):
        """
           Instantiates a list object.
        """
        list.__init__(self)

    def print_sorted(self):
        """A function which prints MyList in ascending order."""
        print(sorted(self))
