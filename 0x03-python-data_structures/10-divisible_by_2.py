#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    by_2 = my_list[:]
    for el in by_2:
        if el % 2 is 0:
            el = True
        else:
            el = False
    return by_2
