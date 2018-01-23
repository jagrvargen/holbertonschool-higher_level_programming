#!/usr/bin/python3
"""
   This module contains unit tests for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """This class contains tests for the Rectangle class."""

    def setUp(self):
        """Set up an instance of a Rectangle to test."""
        self.rectangle = Rectangle(1, 1)

    def test_is_instance(self):
        """
           Test that rectangle is an instance of both the Rectangle and
           Base classes.
        """
        self.assertIsInstance(self.rectangle, Rectangle)
        self.assertIsInstance(self.rectangle, Base)

    def test_attributes(self):
        """Test that attributes are properly set."""
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 1)
        self.assertEqual(self.rectangle.height, 1)
        self.assertEqual(self.rectangle.x, 0)
        self.assertEqual(self.rectangle.y, 0)

    def test_type_error(self):
        """Tests each attribute for proper TypeError exception raising."""
        self.assertRaises(TypeError, self.rectangle, 'check', 1)
        self.assertRaises(TypeError, self.rectangle, 1, 'check')
        self.assertRaises(TypeError, self.rectangle, 1, 1, 'check')
        self.assertRaises(TypeError, self.rectangle, 1, 1, 1, 'check')
        self.assertRaises(TypeError, self.rectangle, (1,), 1,)
        self.assertRaises(TypeError, self.rectangle, [1], 1)

    def test_value_error(self):
        """Tests each attribute for proper ValueError exception raising."""
        self.assertRaises(ValueError, self.rectangle, 0, 1)
        self.assertRaises(ValueError, self.rectangle, 1, 0)
        self.assertRaises(ValueError, self.rectangle, -5, 1)
        self.assertRaises(ValueError, self.rectangle, 1, -5)
        self.assertRaises(ValueError, self.rectangle, 1, 1, -5)
        self.assertRaises(ValueError, self.rectangle, 5, 1, 5, -5)
