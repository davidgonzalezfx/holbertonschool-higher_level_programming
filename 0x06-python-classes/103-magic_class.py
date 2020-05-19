#!/usr/bin/python3
from math import pi
""" From Python Bytecode
    To Python Class 
"""
class MagicClass:
    """Class constructor"""
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """Return the area"""
    def area(self):
        return self.__radius ** 2 * pi

    """Return circumference"""
    def circumference():
        return 2 * pi * self.__radius
