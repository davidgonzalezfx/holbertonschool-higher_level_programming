#!/usr/bin/python3
"""
5-text_identation.py file
Functions:
-> def text_indentation(text)
"""


def text_indentation(text):
    """
    prints a <text> with 2 new lines after each of these characters: ., ? and :
    <text> must be a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    break_line = ['.', '?', ':']

    for ch in range(len(text)):
        if text[ch] is ' ' and text[ch - 1] in break_line:
            continue
        print(text[ch], end='')
        if text[ch] == '.' or text[ch] == '?' or text[ch] == ':':
            print('', end='\n\n')
