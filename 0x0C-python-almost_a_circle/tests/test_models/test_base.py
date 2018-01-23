#!/usr/bin/python3
"""
   This module contains unit tests for the Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class contains unit tests for the Base class."""

    def setUp(self):
        """Set up a Base instance."""
        self.base = Base()

#    def tearDown(self):
#        self.base.dispose()

    def test_type_base(self):
        """Test that base is an instance of the Base class."""
        self.assertIsInstance(self.base, Base)

    def test_nb_objects(self):
        """
           Check that __nb_objects increments and is set to self.id.
           Check that id is set by passing int as parameter.
        """
        self.assertEqual(self.base.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(15)
        self.assertEqual(base3.id, 15)
