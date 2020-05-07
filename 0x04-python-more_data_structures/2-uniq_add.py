#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    uniq_set = set(my_list)
    for el in uniq_set:
        uniq_sum += el
    return uniq_sum
