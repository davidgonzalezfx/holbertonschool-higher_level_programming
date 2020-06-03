#!/usr/bin/python3
"""
files: 2-read_lines.py
functions:
-> read_lines
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file and prints it to stdout """

    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            for line in lines:
                print(line, end='')
        else:
            lines = lines[0:nb_lines]
            for line in lines:
                print(line, end='')
