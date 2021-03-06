#!/usr/bin/python3
"""
   This module contains unit tests for the Square class.
"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """This class contains the unit tests for the Square class."""

    def test_is_instance_square(self):
        """Test if Square() creates a Square instance."""
        s1 = Square(5)
        self.assertIsInstance(s1, Square)

    def test_is_instance_rectangle(self):
        """Test if Square inherits from Rectangle class."""
        s2 = Square(5)
        self.assertIsInstance(s2, Rectangle)

    def test_is_instance_base(self):
        """Test if Square inherits from Base class."""
        s3 = Square(5)
        self.assertIsInstance(s3, Base)

    def test_size_input(self):
        """Test that passing an integer to size parameter has
           correct output.
        """
        s4 = Square(5)
        self.assertEqual(s4.size, 5)

    def test_x_input_square(self):
        """Test that passing an integer to x parameter has correct output."""
        s5 = Square(5, 6)
        self.assertEqual(s5.x, 6)

    def test_y_input_square(self):
        """Test that passing an integer to y parameter has correct output."""
        s6 = Square(5, 6, 7)
        self.assertEqual(s6.y, 7)

    def test_size_type_error(self):
        """Test that passing incorrect type to size parameter
           outputs correct exception.
        """
        self.assertRaises(TypeError, Square, "Harold")
        self.assertRaises(TypeError, Square, [5])
        self.assertRaises(TypeError, Square, (5,))
        self.assertRaises(TypeError, Square, {'size': 5})
        self.assertRaises(TypeError, Square, size="Harold")
        self.assertRaises(TypeError, Square, size=[5])
        self.assertRaises(TypeError, Square, size=(5,))
        self.assertRaises(TypeError, Square, size={'size': 5})
        self.assertRaises(TypeError, Square, 2.5)
        self.assertRaises(TypeError, Square, size=.66)

    def test_x_type_error(self):
        """Test that passing incorrect type to x parameter outputs
           correct error.
        """
        self.assertRaises(TypeError, Square, 1, "Gerald")
        self.assertRaises(TypeError, Square, 1, [5])
        self.assertRaises(TypeError, Square, 1, (5,))
        self.assertRaises(TypeError, Square, 1, {'size': 5})
        self.assertRaises(TypeError, Square, 1, x="Gerald")
        self.assertRaises(TypeError, Square, 1, x=[5])
        self.assertRaises(TypeError, Square, 1, x=(5,))
        self.assertRaises(TypeError, Square, 1, x={'size': 5})
        self.assertRaises(TypeError, Square, 1, 2.5)
        self.assertRaises(TypeError, Square, 1, x=.66)

    def test_y_type_error(self):
        """Test that passing incorrect type to x parameter outputs
           correct error.
        """
        self.assertRaises(TypeError, Square, 1, 1, "Bearold")
        self.assertRaises(TypeError, Square, 1, 1, [5])
        self.assertRaises(TypeError, Square, 1, 1, (5,))
        self.assertRaises(TypeError, Square, 1, 1, {'size': 5})
        self.assertRaises(TypeError, Square, 1, 1, x="Bearold")
        self.assertRaises(TypeError, Square, 1, 1, x=[5])
        self.assertRaises(TypeError, Square, 1, 1, x=(5,))
        self.assertRaises(TypeError, Square, 1, 1, x={'size': 5})
        self.assertRaises(TypeError, Square, 1, 1, 2.5)
        self.assertRaises(TypeError, Square, 1, 1, y=.66)

    def test_size_value_error(self):
        """Test that passing incorrect type to size parameter
           outputs correct exception.
        """
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -50)
        self.assertRaises(ValueError, Square, -9999999999999999)

    def test_x_value_error(self):
        """Test that passing incorrect type to x parameter outputs
           correct error.
        """
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaises(ValueError, Square, 1, -50)
        self.assertRaises(ValueError, Square, 1, -999999999999999)

    def test_y_value_error(self):
        """Test that passing incorrect type to x parameter outputs
           correct error.
        """
        self.assertRaises(ValueError, Square, 1, 1, -1)
        self.assertRaises(ValueError, Square, 1, 1, -50)
        self.assertRaises(ValueError, Square, 1, 1, -99999999999999)

    def test_str_return_square(self):
        """Test that the __str__ method output is correct."""
        s7 = Square(5, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        print(s7)
        sys.stdout = sys.__stdout__
        self.assertEqual("[Square] {:d} 2/2 - 5\n".format(s7.id),
                         output.getvalue())

    def test_display_square(self):
        """Test that the display method output is correct."""
        s8 = Square(3, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        s8.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n  ###\n  ###\n  ###\n", output.getvalue())

    def test_square_size_setter(self):
        """Test that the Square getter method returns."""
        s9 = Square(4, 4, 4)
        self.assertEqual(s9.size, 4)
        self.assertEqual(s9.x, 4)
        self.assertEqual(s9.y, 4)
        s9.size = 6
        self.assertEqual(s9.size, 6)
        s9.x = 6
        self.assertEqual(s9.x, 6)
        s9.y = 6
        self.assertEqual(s9.y, 6)

    def test_update_square(self):
        """Test that the Square update method has correct output."""
        s10 = Square(55, 23, 999)
        self.assertEqual(s10.size, 55)
        self.assertEqual(s10.x, 23)
        self.assertEqual(s10.y, 999)
        s10.update(100, 100, 100, 100)
        self.assertEqual(s10.id, 100)
        self.assertEqual(s10.size, 100)
        self.assertEqual(s10.x, 100)
        self.assertEqual(s10.y, 100)

    def test_update_square_kwargs(self):
        """Test that the Square update method has correct output when
           kwargs are passed.
        """
        s11 = Square(55, 23, 99999)
        self.assertEqual(s11.size, 55)
        self.assertEqual(s11.x, 23)
        self.assertEqual(s11.y, 99999)
        s11.update(x=100, size=100, id=100, y=100)
        self.assertEqual(s11.id, 100)
        self.assertEqual(s11.size, 100)
        self.assertEqual(s11.x, 100)
        self.assertEqual(s11.y, 100)

    def test_to_dictionary_square(self):
        """Test that the Square to_dictionary method returns a
           valid dictionary.
        """
        s12 = Square(id=5, size=222, x=777, y=8888)
        s_dict = s12.to_dictionary()
        self.assertEqual(s_dict, {'x': 777, 'y': 8888, 'size': 222, 'id': 5})

    def test_to_dictionary_square(self):
        """Test that the Rectangle to_dictionary method returns a
           valid dictionary.
        """
        s11 = Square(id=5, size=222, x=777, y=8888)
        s_dict = s11.to_dictionary()
        self.assertEqual(s_dict, {'x': 777, 'y': 8888, 'size': 222,
                                  'id': 5})

    def test_from_json_string_square(self):
        """Test that from_json_string method returns list of dictionaries
           from a JSON string.
        """
        list_input = [{'id': 89, 'size': 10},
                      {'id': 7, 'size': 1}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)
