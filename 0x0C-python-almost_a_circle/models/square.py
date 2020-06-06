#!/usr/bin/python3
'''
file: square.py
classes:
-> Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square model, inherits from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Constructor method '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        ''' [Rectangle] (<id>) <x>/<y> - <width>/<height> '''
        txt = '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)
        return txt
