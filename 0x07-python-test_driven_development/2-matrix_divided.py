#!/usr/bin/python3
"""This is module 2-matrix_divided
This module supplies one function, add_integer().  For example,
>>> matrix_divided([[0, 2][4, 6]], 2)
[[0.0, 1.0], [2.0, 3.0]]
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.
    matrix: list of a list
    div: int or float different from 0"""
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not type(matrix) == list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for elmt in matrix:
        if not isinstance(elmt, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if (len(matrix[0]) == 0):
        return matrix

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not type(div) == int and not type(div) == float:
        raise TypeError("div must be a number")

    size = len(matrix)
    new = [[0 for _ in range(len(matrix[0]))] for _ in range(size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            new[i][j] = round((matrix[i][j] / div), 2)
    return new
