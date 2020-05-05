#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) is 0:
        cp_a = (0, 0)
    elif len(tuple_a) is 1:
        cp_a = (tuple_a[0], 0)
    elif len(tuple_a) > 1:
        cp_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) is 0:
        cp_b = (0, 0)
    elif len(tuple_b) is 1:
        cp_b = (tuple_b[0], 0)
    elif len(tuple_a) > 1:
        cp_b = (tuple_b[0], tuple_b[1])

    return (cp_a[0] + cp_b[0], cp_a[1] + cp_b[1])
