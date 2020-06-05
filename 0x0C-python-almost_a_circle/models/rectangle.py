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
        ''' Constructor method '''
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    ''' Getters '''
    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    ''' Setters '''
    @x.setter
    def x(self, value):
        ''' x setter '''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        ''' y setter '''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        ''' height setter '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be >= 0')
        self.__height = value
