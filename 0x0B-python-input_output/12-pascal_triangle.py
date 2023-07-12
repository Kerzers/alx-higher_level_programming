#!/usr/bin/python3
""" module defines function: pascal_triange """


def pascal_triangle(n):
    """function that returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    triangle = []
    if n <= 0:
        return triangle
    triangle = list(list(0 for _ in range(i + 1)) for i in range(n))
    for i in range(n):
        if i == 0:
            triangle[0][0] = 1
        for j in range(i):
            triangle[i][0] = 1
            triangle[i][i] = 1
            for k in range(1, j + 1):
                triangle[i][j] = triangle[i - 1][k - 1] + triangle[i - 1][k]

    return triangle
