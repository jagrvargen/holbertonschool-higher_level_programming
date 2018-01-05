#!/usr/bin/python3


def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix """
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
