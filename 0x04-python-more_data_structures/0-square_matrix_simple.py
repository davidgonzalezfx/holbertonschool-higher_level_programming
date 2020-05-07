#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[el ** 2 for el in row] for row in matrix]
    return (square_matrix)
