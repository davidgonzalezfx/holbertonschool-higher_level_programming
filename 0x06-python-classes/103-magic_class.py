#!/usr/bin/python3
from math import pi
class MagicClass:
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
        
    def area(self):
        return self.__radius ** 2 * pi

    def circumference():
        return 2 * pi * self.__radius
