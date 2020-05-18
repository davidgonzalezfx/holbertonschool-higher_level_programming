#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(x):
            print('{}'.format(my_list[idx]), end='')
        print()
        return x
    except IndexError:
        print()
        return idx
