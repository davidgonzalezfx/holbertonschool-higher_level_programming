#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a_key, a_value in a_dictionary.items():
        if value is a_value:
            a_dictionary.pop(a_key)
    return a_dictionary
