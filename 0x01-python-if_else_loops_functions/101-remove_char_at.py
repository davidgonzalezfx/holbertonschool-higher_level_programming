#!/usr/bin/python3
def remove_char_at(str, n):
    str_cp = ''
    for i in range(0, len(str)):
        if i != n:
            str_cp += str[i]
    return str_cp
