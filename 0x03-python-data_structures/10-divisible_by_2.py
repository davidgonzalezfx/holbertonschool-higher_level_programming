#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    by_2 = my_list[:]
    for idx in range(0, len(by_2)):
        if by_2[idx] % 2 is 0:
            by_2[idx] = True
        else:
            by_2[idx] = False
    return by_2
