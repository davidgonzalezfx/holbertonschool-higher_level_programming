#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list and x > 0:
        try:
            for idx in range(x):
                print('{}'.format(my_list[idx]), end='')
            print()
            return idx + 1
        except IndexError:
            print()
            return idx - 1
    else:
        return 0
