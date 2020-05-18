#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list and x > 0:
        try:
            for idx, el in enumerate(my_list):
                print('{}'.format(el), end='')
            print()
            return idx
        except:
            print()
            return idx
    else:
        return 0