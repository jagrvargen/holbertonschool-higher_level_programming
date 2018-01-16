#!/usr/bin/python3
"""A module conataining a function that prints the phrase 'My name is {} {}'.

   first_name (string): A non-empty string value.
   last_name (string): A string value.
"""

def say_my_name(first_name, last_name=""):
    """
       A function that prints 'My name is {} {}'.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
