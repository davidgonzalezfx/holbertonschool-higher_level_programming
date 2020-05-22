#!/usr/bin/python3
"""
4-print_square.py file
Functions:
-> print_square(size)
"""


def print_square(size):
    """
    prints a square with the character #
    size is the size length of the square
    size must be an integer
    size must be greater than zero
    size can not be float and less than zero
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for n in range(size):
        print('#' * size)
