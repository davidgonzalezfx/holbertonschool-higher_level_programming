#!/usr/bin/python3
"""
file: 1-number_of_lines.py
functions:
-> number_of_lines
"""


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """

    with open(filename) as file:
        lines = file.readlines()
    return len(lines)
