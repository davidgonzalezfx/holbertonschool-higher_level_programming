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
    
    def update(self, *args, **kwargs):
        ''' assigns an argument to each attribute '''
        available = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for attr in range(0, len(args)):
                setattr(self, available[attr], args[attr])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        ''' [Rectangle] (<id>) <x>/<y> - <width>/<height> '''
        txt = '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)
        return txt
