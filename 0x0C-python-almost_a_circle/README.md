			Python - Almost a Circle Project

This is a 5-day project intended to promote a deep and practical understanding of the Python3 unittest unit testing framework module.

0. tests/ - Create a directory tests in which to begin the process of creating unit tests.

1. models/base.py - This module lays out the foundation for the Base class, which all other classes will be based upon.

2. models/rectangle.py - This module defines the Rectangle class, which inherits from base. The private instance attributes __width, __height, __x, and __y are defined. The private instance attribute is is instantiated by a call to the superclass, Base.

3. The Rectangle class is updated with exceptions for TypeError and ValueError for all setter methods.

4. Add the public method area(self) to the Rectangle class which returns the Rectangle instance's area..

5. Add the public method display(self) which prints the rectangle using the # character.

6. Add and overload the __str__ method which returns "[Rectangle] <x>/<y> - <width/<height>>".

7. Update the display method to print account for the starting x and y coordinates.

8. Update the Rectangle class by adding the public method update(self, *args) that assigns an argument to each attribute.

9. Update the Rectangle method to include **kwargs.

10. Add the Square class which inherits from Rectangle. Calls the superclass to inherit all attributes. The width and height attributes become size.

11. Update the Square class by adding the getter and setter moethods for the size attribute.

12. Update the Square class by adding the update() method, which assigns and updates an instance's attributes.

13. Update the Rectangle class by adding the public method to_dictionary(), which returns the dictionary representation of a Rectangle instance.
