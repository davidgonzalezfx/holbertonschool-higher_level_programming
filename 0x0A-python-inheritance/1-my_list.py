#!/usr/bin/python3
"""
file: 1-mi_list.py
Class:
-> MyList
"""


class MyList(list):
    """ class MyList that inherits from list """

    def print_sorted(self):
        print(sorted(self))
        