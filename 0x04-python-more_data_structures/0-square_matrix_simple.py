#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function that computes the square value of all
    integers of a matrix"""
    squares = [[x**2 for x in row] for row in matrix]
    return squares
