#!/usr/bin/python3
'''
file: base..py
classes:
-> Base
'''
import json


class Base:
    ''' Base class manage id attribute in all your future classes '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Constructor method '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        ''' Dictionary to JSON string '''
        if list_dictionaries is None or list_dictionaries is []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
