#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Class for unit testing """

    def test_normal_case(self):
        self.assertEqual(max_integer([1, 2,]), 2)

    def test_one_case(self):
        self.assertEqual(max_integer([10]), 10)

    def test_repeated_case(self):
        self.assertEqual(max_integer([1, 3, 2, 3]), 3)

    def test_negative_case(self):
        self.assertEqual(max_integer([-1, -2]), -1)

    def test_float_case(self):
        self.assertEqual(max_integer([1.1, 2.5, 1.7, 2.4]), 2.5)
        self.assertEqual(max_integer([1.1, -2.5, -1.7, -2.4]), 1.1)


    def test_string_case(self):
        self.assertEqual(max_integer(["aaaab", "aaaz"]), "aaaz")
        self.assertEqual(max_integer(["aaab", "Aaaz"]), "aaab")
        self.assertEqual(max_integer(["a", "z"]), "z")

    def test_bool_case(self):
        self.assertEqual(max_integer([False, True]), True)
        self.assertEqual(max_integer([False, False]), False)
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([True, True]), True)
        self.assertEqual(max_integer([1, False]), 1)

    def test_list_of_list_case(self):
        self.assertEqual(max_integer([[1, 0], [2, 0]]), [2, 0])
        self.assertEqual(max_integer([(1, 0), (2, 0)]), (2, 0))

    def test_empty_case(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer(()), None)
    
    def test_none_case(self):
        self.assertRaises(TypeError, max_integer, [None, None])

    def test_mix_case(self):
        self.assertRaises(TypeError, max_integer, [1, 'str', True])
        self.assertRaises(TypeError, max_integer, [1, [2, 3], True])
        self.assertRaises(TypeError, max_integer, [1, [2, 3], {4, 5}])
        self.assertRaises(TypeError, max_integer, [1, (2, 3), None])
    
    def test_one_num(self):
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.1)
