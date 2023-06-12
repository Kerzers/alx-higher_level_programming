#!/usr/bin/python3
"""function that prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            if j == len(row) - 1:
                print("{:d}".format(row[j]), end='')
            else:
                print("{:d}".format(row[j]), end=' ')
        print()
