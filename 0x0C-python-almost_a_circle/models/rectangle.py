#!/usr/bin/python3
'''
file: rectangle.py
classes:
-> Rectangle
'''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle model, inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    ''' Getters '''
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    ''' Setters '''
    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value
