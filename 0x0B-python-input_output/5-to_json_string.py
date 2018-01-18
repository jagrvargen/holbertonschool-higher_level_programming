#!/usr/bin/python3
"""
   This module contains a function which returns the JSON string
   representation of an object.
"""
import json


def to_json_string(my_obj):
    """A function which returns the JSON representation of an object."""
    return json.dumps(my_obj)
