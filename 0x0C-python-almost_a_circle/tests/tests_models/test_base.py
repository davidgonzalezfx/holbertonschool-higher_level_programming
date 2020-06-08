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


class test_constructor(unittest.TestCase):
    ''' tests for Base Class Constructor Method '''

    def test_no_args(self):
        ''' no arguments passed '''
        pass

    def test_none(self):
        ''' None as argument '''
        pass

    def test_auto_id(self):
        ''' Check auto id assignment '''
        pass

    def test_id_normal(self):
        ''' int arguments '''
        pass

    def test_private_attr(self):
        ''' Check private __nb_objects attr '''
        pass


class test_inheritance(unittest.TestCase):
    ''' tests for inheritance and types'''

    def test_type(self):
        ''' object created is instance '''
        pass

    def test_r_is_base(self):
        ''' rectangle is base instance '''
        pass

    def test_s_is_base(self):
        ''' square is base instance '''
        pass


class test_to_json(unittest.TestCase):
    ''' tests for to_json_string method'''

    def test_no_args(self):
        ''' no arguments passed '''
        pass

    def test_none(self):
        ''' None as argument '''
        pass

    def test_empty_list(self):
        ''' empty list [] '''
        pass

    def test_empty_dict(self):
        ''' list with empty dict [{}] '''
        pass

    def test_normal(self):
        ''' list and dictonaries normally '''
        pass

    def test_normal_rectangle(self):
        ''' rectangles to json '''
        pass

    def test_normal_square(self):
        ''' squares to json '''
        pass

    def test_return_type(self):
        ''' to_json_string must return str '''
        pass


class test_from_json(unittest.TestCase):
    ''' tests for from_json_string method'''

    def test_no_args(self):
        ''' no arguments passed '''
        pass

    def test_none(self):
        ''' None as argument '''
        pass

    def test_empty_list(self):
        ''' json empty list [] '''
        pass

    def test_empty_dict(self):
        ''' json list with empty dict [{}] '''
        pass

    def test_normal(self):
        ''' list and dictonaries normally '''
        pass

    def test_normal_rectangle(self):
        ''' rectangles to json '''
        pass

    def test_normal_square(self):
        ''' squares to json '''
        pass

    def test_return_type(self):
        ''' to_json_string must return str '''
        pass


class test_create(unittest.TestCase):
    ''' test for create method '''

    def test_rectangles(self):
        ''' Rectangle instances '''
        pass

    def test_squares(self):
        ''' Squares instances '''
