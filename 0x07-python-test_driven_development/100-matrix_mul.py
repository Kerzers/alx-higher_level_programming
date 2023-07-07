#!/usr/bin/python3
"""This is module matrix_mul
it defines a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ it multiplies 2 mrtices
    m_a and m_b must be an list of lists of integers or floats
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
    if not m_a or all(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or all(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        for elmt in m_a[i]:
            if not isinstance(elmt, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        for elmt in m_b[i]:
            if not isinstance(elmt, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    prod = [[0 for i in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                prod[i][j] += m_a[i][k] * m_b[k][j]
    return prod
