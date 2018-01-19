#!/usr/bin/python3
"""
   This module contains the class definition for Base. Which forms the base
   for all other classes in the 'almost a circle' project.
"""


class Base:
    """This class will form the base for all classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
           Instantiates a Base object instance. If id is not None,
           it assigns the public instance attribute id.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects