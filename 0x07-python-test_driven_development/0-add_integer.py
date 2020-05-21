#!/usr/bin/python3
""" 
0-add_integer.py file
Functions:
-> add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """ Adds two integers (a and b)
    a and b should be int or float type
    return int addition """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
