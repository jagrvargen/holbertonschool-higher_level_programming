#!/usr/bin/python3
"""
   This module contains a function which will serialize a class to JSON
    format.
"""


def class_to_json(obj):
    """Returns a JSON serialized version of an object."""
    my_dict = {}
    for key, value in obj.__dict__.items():
        my_dict[key] = value
    return my_dict
