#!/usr/bin/python3
"""
   This module contains a function which creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file."""
    with open(filename, encoding="utf-8") as fp:
        return json.load(fp)
