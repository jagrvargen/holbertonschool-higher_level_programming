#!/usr/bin/python3
"""
   This module contains a function which determines if an object is of
   a specified class.
"""


def is_same_class(obj, a_class):
    """
       A function which returns True if the object is exactly an instance
       of the specified class; otherwise False.
    """
    return type(obj) == a_class:
