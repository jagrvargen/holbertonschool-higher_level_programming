#!/usr/bin/python3
"""
   This module contains unit tests for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """This class contains tests for the Rectangle class."""

    def test_is_instance(self):
        """
           Test that rectangle is an instance of both the Rectangle and
           Base classes.
        """
        r1 = Rectangle(1, 1)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

    def test_attributes(self):
        """Test that attributes are properly set."""
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_type_error(self):
        """Tests each attribute for proper TypeError exception raising."""
        self.assertRaises(TypeError, Rectangle, 'check', 1)
        self.assertRaises(TypeError, Rectangle, 1, 'check')
        self.assertRaises(TypeError, Rectangle, 1, 1, 'check')
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, 'check')
        self.assertRaises(TypeError, Rectangle, (1,), 1,)
        self.assertRaises(TypeError, Rectangle, [1], 1)

    def test_value_error(self):
        """Tests each attribute for proper ValueError exception raising."""
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, -5, 1)
        self.assertRaises(ValueError, Rectangle, 1, -5)
        self.assertRaises(ValueError, Rectangle, 1, 1, -5)
        self.assertRaises(ValueError, Rectangle, 5, 1, 5, -5)

    def test_area_method(self):
        """Tests the area method output."""
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.area(), 1)
        r4 = Rectangle(250, 2, 60, 80)
        self.assertEqual(r4.area(), 500)

#    def test_str(self):
#        """Tests the ouput for the __str__ method."""
#        r5 = Rectangle(5, 6, 7, 8)
#        self.assertEqual(print(r5), "[Rectangle] (8) 7/8 - 5/6")

    def test_update_rectangle(self):
        """Test the output of the Rectangle class"""
        with self.assertRaises(TypeError):
            r6 = Rectangle()
        r6 = Rectangle(1, 1, 1, 1)
        r6.update(5, 1)
        self.assertEqual(r6.id, 5)
        r6.update(5, 5)
        self.assertEqual(r6.width, 5)
        r6.update(2, 2, 5)
        self.assertEqual(r6.height, 5)
        r6.update(3, 3, 4, 5)
        self.assertEqual(r6.x, 5)
        r6.update(4, 4, 5, 6, 5)
        self.assertEqual(r6.y, 5)
