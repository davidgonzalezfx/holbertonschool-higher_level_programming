#!/usr/bin/python3
'''
file: base..py
classes:
-> Base
'''
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Dictionary to JSON string '''
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        ''' JSON string to file '''
        obj_dict = []
        if list_objs:
            for obj in list_objs:
                obj_dict.append(obj.to_dictionary())

        with open(cls.__name__ + '.json', 'w') as json_file:
            json_file.write(cls.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        ''' JSON string to dictionary '''
        if json_string and len(json_string) > 0:
            json.loads(json_string)

        return []

    @classmethod
    def create(cls, **dictionary):
        ''' Dictionary to Instance '''
        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 1)
        elif cls.__name__ == 'Square':
            tmp = cls(1)

        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        ''' File to instances '''
        try:
            with open(cls.__name__ + '.json', 'r') as file:
                json_str = file.read()
                list_dict = Base.from_json_string(json_str)
                list_objs = []
                for obj_dict in list_dict:
                    list_objs.append(cls.create(**obj_dict))
                return list_objs
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' JSON ok, but CSV? - save '''
        f_name = cls.__name__ + '.csv'
        with open(f_name, 'w', encoding='utf-8') as file:
            if list_objs is None or len(list_objs) == 0:
                file.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    attrs = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    attrs = ['id', 'size', 'x', 'y']

                file_csv = csv.DictWriter(file, fieldnames=attrs)
                for obj in list_objs:
                    file_csv.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv data """
        f_name = cls.__name__ + '.csv'
        try:
            with open(f_name, 'r', encoding='utf-8') as file:
                if cls.__name__ == 'Rectangle':
                    attrs = ['id', 'width', 'height', 'x', 'y']
                else:
                    attrs = ['id', 'size', 'x', 'y']

                csv_dict = csv.DictReader(file, fieldnames=attrs)
                list_dict = []
                for row in csv_dict:
                    new_dict = {}
                    for key, val in row.items():
                        new_dict[key] = int(val)
                    list_dict.append(new_dict)

                saved = []
                for obj in list_dict:
                    saved.append(cls.create(**obj))
                return saved
        except IOError:
            return []
