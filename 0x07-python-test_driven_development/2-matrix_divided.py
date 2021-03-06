#!/usr/bin/python3
"""A module which defines a function for dividing elements of a matrix.

   matrix (list): A list of lists containing integer or floating point values.    The length of the lists must be consistent.
   div (int) | (float): An integer or floating point value which cannot be
   equal to zero (in order to avoid a DivisionByZeroError).
"""

def matrix_divided(matrix, div):
    """
       A function that divides all elements of a matrix
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers\
/floats")
    listLen = len(matrix[0])

    for i in matrix:
        if len(i) != listLen:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    myMatrix = [[round(x / div, 2) for x in y] for y in matrix]

    return myMatrix
