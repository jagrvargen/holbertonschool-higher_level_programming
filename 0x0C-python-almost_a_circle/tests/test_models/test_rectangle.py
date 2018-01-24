#!/usr/bin/python3
"""
   This module contains unit tests for the Rectangle class.
"""
import unittest
import sys
import io
import json
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

    def test_str_return_square(self):
        """Test that the __str__ method output is correct."""
        r = Rectangle(5, 2, 2, 3)
        output = io.StringIO()
        sys.stdout = output
        print(r)
        sys.stdout = sys.__stdout__
        self.assertEqual("[Rectangle] {:d} 2/3 - 5/2\n".format(r.id),\
                         output.getvalue())

    def test_update_rectangle_args(self):
        """Test the attributes of the Rectangle class when no-keyword args
           are passed to the update method.
        """
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

    def test_update_rectangle_kwargs(self):
        """Test the attributes of the Rectangle class when keyword args
           are passed to the update method.
        """
        r7 = Rectangle(1, 1, 1, 1)
        r7.update(id=5, width=1)
        self.assertEqual(r7.id, 5)
        r7.update(id=5, width=5)
        self.assertEqual(r7.width, 5)
        r7.update(id=2, width=2, height=5)
        self.assertEqual(r7.height, 5)
        r7.update(id=3, width=3, height=4, x=5)
        self.assertEqual(r7.x, 5)
        r7.update(id=4, width=4, height=5, x=6, y=5)
        self.assertEqual(r7.y, 5)
        self.assertEqual(r7.width, 4)
        self.assertEqual(r7.height, 5)
        self.assertEqual(r7.x, 6)

    def test_display_output(self):
        """Tests the display method for correct output."""
        r8 = Rectangle(width=3, height=3)
        output = io.StringIO()
        sys.stdout = output
        r8.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("###\n###\n###\n", output.getvalue())

    def test_display_output_with_offset(self):
        """Test the display method including offset values."""
        r9 = Rectangle(width=5, height=3, x=4, y=2)
        output = io.StringIO()
        sys.stdout = output
        r9.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n    #####\n    #####\n    #####\n",\
                         output.getvalue())

    def test_to_dictionary_rectangle(self):
        """Test that the Rectangle to_dictionary method returns a
           valid dictionary.
        """
        r10 = Rectangle(id=5, width=222, height=555, x=777, y=8888)
        r_dict = r10.to_dictionary()
        self.assertEqual(r_dict, {'x': 777, 'y': 8888, 'width': 222,\
                                  'height': 555, 'id': 5})

    def test_save_to_file_rectangle(self):
        """Test that the save_to_file method writes a JSON string
           representation of a list of objects to a file.
        """
        r11 = Rectangle(44, 33, 22, 11)
        Rectangle.save_to_file([r11])
        with open("Rectangle.json", "r") as fp:
            json_string = fp.read()
        self.assertIsInstance(json_string, str)

    def test_from_json_string_base(self):
        """Test that from_json_string method returns list of dictionaries
           from a JSON string.
        """
        list_input = [{'id': 89, 'width': 10, 'height': 4},\
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_create_rectangle(self):
        """Test that create method returns a new instance of a
           Square with all attributes set.
        """
        r12 = Rectangle(3, 5, 6, 8, 9)
        r12_dict = r12.to_dictionary()
        output = io.StringIO()
        sys.stdout = output
        print(r12)
        sys.stdout = sys.__stdout__
        self.assertEqual("[Rectangle] 9 6/8 - 3/5\n", output.getvalue())
