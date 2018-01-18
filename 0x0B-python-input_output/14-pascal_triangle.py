#!/usr/bin/python3
"""
   This module contains a function which returns a list of integers
   representing Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Returns Pascal's triangle of n"""
    triangle = [1]
    block = 1
    for row in range(1, n):
        for num in range(0, block):
            if num == 0 or num == block - 1:
                triangle.append([1])
            elif num < 
    return triangle
