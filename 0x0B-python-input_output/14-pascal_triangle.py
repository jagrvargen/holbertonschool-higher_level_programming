#!/usr/bin/python3
"""
   This module contains a function which returns a list of integers
   representing Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Returns Pascal's triangle of n"""
    triangle = [[1]]

    for x in range(1, n):
        row = [1]
        for block in range(1, x):
            row.append(triangle[x - 1][block] + triangle[x - 1][block - 1])
        row.append(1)
        triangle.append(row)
    return triangle
