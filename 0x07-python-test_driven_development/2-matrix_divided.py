#!/usr/bin/python3
"""
2-matrix_divided.py file
Functions:
-> matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    matrix must be a list of lists of integers or floats
    Each row of the matrix must be of the same size
    div must be a number (integer or float) not 0
    Returns a new matrix with element divided by div
    """

    matrix_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if (not matrix or type(matrix) is not list
            or matrix is []
            or not all([type(row) is list for row in matrix])
            or not all([all([isinstance(el, (int, float)) for el in row]) for row in matrix])):
        raise TypeError(matrix_error)


    if len(set([len(rows) for rows in matrix])) is not 1:
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return  [[round(elmnt / div, 2) for elmnt in row] for row in matrix]
