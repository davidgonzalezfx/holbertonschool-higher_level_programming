#!/usr/python3
'''
File: test_base.py
Classes:
-> test_constructor
-> test_inheritance
-> test_to_json
-> test_from_json
-> test_create
->
'''
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_constructor(unittest.TestCase):
    ''' tests for Base Class Constructor Method '''

    def setUp(self):
        ''' Set up for all methods '''
        Base._Base__nb_objects = 0

    def test_no_args(self):
        ''' no arguments passed '''
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_none_auti(self):
        ''' None as argument '''
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_normal(self):
        ''' int arguments - id assignment'''
        obj1 = Base(1)
        self.assertEqual(obj1.id, 1)
        obj0 = Base(None)
        self.assertEqual(obj0.id, 1)
        obj2 = Base(-2)
        self.assertEqual(obj2.id, -2)
        obj_2 = Base()
        self.assertEqual(obj_2.id, 2)
        obj3 = Base(100)
        self.assertEqual(obj3.id, 100)
        obj4 = Base(1024)
        self.assertEqual(obj4.id, 1024)

    def test_private_attr(self):
        ''' Check private __nb_objects attr '''
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects


class test_inheritance(unittest.TestCase):
    ''' tests for inheritance and types'''

    def test_type(self):
        ''' object created is instance '''
        obj = Base(1)
        self.assertTrue(isinstance(obj, Base))

    def test_r_is_base(self):
        ''' rectangle is base instance '''
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertTrue(isinstance(r, Base))

    def test_s_is_base(self):
        ''' square is base instance '''
        s = Rectangle(1, 1, 1, 1)
        self.assertTrue(isinstance(s, Base))


class test_to_json(unittest.TestCase):
    ''' tests for to_json_string method'''

    def test_no_args(self):
        ''' no arguments passed '''
        with self.assertRaises(TypeError):
            self.assertEqual(Base.to_json_string(), '[]')

    def test_none(self):
        ''' None as argument '''
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_empty_list(self):
        ''' empty list [] '''
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_empty_dict(self):
        ''' list with empty dict [{}] '''
        self.assertEqual(Base.to_json_string([{}]), '[{}]')

    def test_normal(self):
        ''' list and dictonaries normally '''
        objs = [
            {'id': 1, 'width': 3, 'height': 1},
            {'id': 2, 'width': 4, 'height': 4, 'x': 2, 'y': 2},
            {'id': 3}
        ]
        jsonify = Base.to_json_string(objs)
        self.assertEqual(json.loads(jsonify), objs)

    def test_normal_rectangle(self):
        ''' rectangles to json '''
        r = Rectangle(3, 4, 10, 10)
        r1 = Rectangle(5, 1)
        check = [r.to_dictionary(), r1.to_dictionary()]
        jsonify = Base.to_json_string(check)
        self.assertEqual(json.loads(jsonify), check)

    def test_normal_square(self):
        ''' squares to json '''
        s = Square(2, 2, 2)
        s1 = Square(5)
        check = [s.to_dictionary(), s1.to_dictionary()]
        jsonify = Base.to_json_string(check)
        self.assertEqual(json.loads(jsonify), check)

    def test_return_type(self):
        ''' to_json_string must return str '''
        objs = [
            {'id': 2, 'width': 4, 'height': 4, 'x': 2, 'y': 2}
        ]
        jsonify = Base.to_json_string(objs)
        self.assertEqual(type(jsonify), str)


class test_from_json(unittest.TestCase):
    ''' tests for from_json_string method'''

    def test_no_args(self):
        ''' no arguments passed '''
        with self.assertRaises(TypeError):
            self.assertEqual(Base.from_json_string(), '[]')

    def test_none(self):
        ''' None as argument '''
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_str(self):
        ''' empty json string '''
        self.assertEqual(Base.from_json_string(''), [])

    def test_empty_list(self):
        ''' json empty list [] '''
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_empty_dict(self):
        ''' json list with empty dict [{}] '''
        self.assertEqual(Base.from_json_string('[{}]'), [{}])

    def test_normal(self):
        ''' list and dictonaries normally '''
        init = '''[
            {"id": 1, "width": 3, "height": 1},
            {"id": 2, "width": 4, "height": 4, "x": 2, "y": 2},
            {"id": 3}
        ]'''
        check = [
            {'id': 1, 'width': 3, 'height': 1},
            {'id': 2, 'width': 4, 'height': 4, 'x': 2, 'y': 2},
            {'id': 3}
        ]
        self.assertEqual(Base.from_json_string(init), check)

    def test_normal_rectangle(self):
        ''' rectangles to json '''
        init = '''[
            {"id": 1, "width": 3, "height": 4, "x": 10, "y": 10},
            {"id": 6, "width": 5, "height": 1, "x": 0, "y": 0}
        ]'''
        r = Rectangle(3, 4, 10, 10, 1)
        r1 = Rectangle(5, 1)
        check = [r.to_dictionary(), r1.to_dictionary()]
        self.assertEqual(Base.from_json_string(init), check)

    def test_normal_square(self):
        ''' squares to json '''
        init = '''[
            {"id": 10, "size": 2, "x": 2, "y": 2},
            {"id": 7, "size": 5, "x": 0, "y": 0}
        ]'''
        s = Square(2, 2, 2, 10)
        s1 = Square(5)
        check = [s.to_dictionary(), s1.to_dictionary()]
        self.assertEqual(Base.from_json_string(init), check)

    def test_return_type(self):
        ''' to_json_string must return str '''
        init = '[{"id": 1, "size": 3}]'
        check = [{'id': 1, 'size': 3}]
        tp = Base.from_json_string(init)
        self.assertEqual(tp, check)
        self.assertTrue(type(tp), list)
        self.assertTrue(type(tp[0]), dict)


class test_create(unittest.TestCase):
    ''' test for create method '''

    def test_rectangles(self):
        ''' Rectangle instances '''
        r = Rectangle(3, 4, 10, 10)
        check = Rectangle.create(**r.to_dictionary())
        self.assertFalse(r is check)
        self.assertFalse(r == check)

    def test_squares(self):
        ''' Squares instances '''
        r = Square(5)
        check = Rectangle.create(**r.to_dictionary())
        self.assertFalse(r is check)
        self.assertFalse(r == check)


class tests_save_file(unittest.TestCase):
    ''' test for save_to_file method '''

    def tearDown(self):
        ''' Executed after each class method '''
        try:
            remove('Rectangle.json')
        except BaseException:
            pass
        try:
            remove('Square.json')
        except BaseException:
            pass

    def test_none_rectangle(self):
        ''' None as argument - Rectangle '''
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile('Rectangle.json'))
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_none_square(self):
        ''' None as argument - Square '''
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile('Square.json'))
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_empty_list(self):
        ''' Empty list - Rectangle '''
        arg = []
        Square.save_to_file(arg)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_empty_list_square(self):
        ''' Empty list - Square '''
        arg = []
        Square.save_to_file(arg)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_rectangle(self):
        ''' Rectangle instances '''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        arg = [r1, r2]
        check = """[{"id": 13, "width": 10, "height": 7, "x": 2, "y": 8}, """
        check = check + '{"id": 14, "width": 2, "height": 4, "x": 0, "y": 0}]'

        Rectangle.save_to_file(arg)
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(file.read(), check)

    def test_square(self):
        ''' Square instances '''
        s1 = Square(7, 2, 8)
        s2 = Square(2)
        arg = [s1, s2]
        check = """[{"id": 15, "size": 7, "x": 2, "y": 8}, """
        check = check + """{"id": 16, "size": 2, "x": 0, "y": 0}]"""
        Square.save_to_file(arg)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), check)


class Test_load_file(unittest.TestCase):
    ''' test for load_from_file method '''

    def tearDown(self):
        ''' Executed after each class method '''
        try:
            remove('Rectangle.json')
        except BaseException:
            pass
        try:
            remove('Square.json')
        except BaseException:
            pass

    def test_not_found(self):
        ''' File not found '''
        arg = Rectangle.load_from_file()
        check = []
        self.assertEqual(arg, check)

    def test_empty_file_list(self):
        ''' Empty list - Rectangle '''
        Rectangle.save_to_file([])
        arg = Rectangle.load_from_file()
        check = []
        self.assertEqual(arg, check)

    def test_rectangle(self):
        ''' Rectangle instances '''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 0, 0, 1)
        file = Rectangle.save_to_file([r1, r2])
        load = Rectangle.load_from_file()
        r3 = load[0].to_dictionary()
        r4 = load[1].to_dictionary()

        self.assertEqual(type(load), list)
        self.assertEqual(type(load[0]), Rectangle)
        self.assertEqual(r3, r1.to_dictionary())
        self.assertEqual(r4, r2.to_dictionary())

    def test_square(self):
        ''' Square instances '''
        s1 = Square(10, 2, 8)
        s2 = Square(2, 0, 0, 1)
        file = Square.save_to_file([s1, s2])
        load = Square.load_from_file()
        s3 = load[0].to_dictionary()
        s4 = load[1].to_dictionary()

        self.assertEqual(type(load), list)
        self.assertEqual(type(load[0]), Square)
        self.assertEqual(s3, s1.to_dictionary())
        self.assertEqual(s4, s2.to_dictionary())
