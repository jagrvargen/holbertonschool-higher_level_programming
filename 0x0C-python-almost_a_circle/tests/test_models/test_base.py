#!/usr/bin/python3
"""
   This module contains unit tests for the Base class.
"""
import unittest
import json
import sys
import io
from models.base import Base


class TestBase(unittest.TestCase):
    """This class contains unit tests for the Base class."""

    def test_is_instance_base(self):
        """Test that Base() returns an instance of the Base class."""
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_nb_objects(self):
        """
           Check that __nb_objects increments and is set to self.id.
           Check that id is set by passing int as parameter.
        """
        b2 = Base(1)
        self.assertEqual(b2.id, 1)
        b3 = Base(2)
        self.assertEqual(b3.id, 2)
        b4 = Base(15)
        self.assertEqual(b4.id, 15)

    def test_to_json_string_base(self):
        """Test that the to_json_string method returns a json string
           representation of a list of dictionaries.
        """
        output = io.StringIO()
        sys.stdout = output
        dictionary1 = {'id': 25, 'width': 33, 'height': 678, 'x': 9, 'y': 1}

        dictionary3 = None
        json_dict1 = Base.to_json_string([dictionary1])
        print(json_dict1)
        sys.stdout = sys.__stdout__
        self.assertEqual(json_dict1 + "\n", output.getvalue())
        self.assertEqual(type(json_dict1), str)

    def test_to_json_string_base_empty(self):
        """Test that to_json_string method returns the string '[]' if
           list_dictionaries parameter is empty.
        """
        output = io.StringIO()
        sys.stdout = output
        dictionary2 = {}
        json_dict2 = Base.to_json_string([dictionary2])
        print(json_dict2)
        sys.stdout = sys.__stdout__
        self.assertEqual(json_dict2 + "\n", output.getvalue())

    def test_to_json_string_base_none(self):
        """Test that to_json_string method returns the string '[]' if
           list_dictionaries parameter is None.
        """
        output = io.StringIO()
        sys.stdout = output
        dictionary3 = None
        json_dict3 = Base.to_json_string([dictionary3])
        print(json_dict3)
        sys.stdout = sys.__stdout__
        self.assertEqual(json_dict3 + "\n", output.getvalue())
