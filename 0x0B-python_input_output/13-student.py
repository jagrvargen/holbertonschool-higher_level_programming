#!/usr/bin/python3
"""
   A module containing the class definition Student.
"""


class Student:
    """A class which defines a student object."""
    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        my_dict = {}
        if type(attrs) == list:
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
        else:
            for key, value in self.__dict__.items():
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of an instance."""
        for key, value in self.__dict__.items():
            if key in json:
                self.__dict__[key] = json[key]
