#!/usr/bin/python3
def search_replace(my_list, search, replace):
    changed = []
    for el in my_list:
        if el == search:
            changed.append(replace)
        else:
            changed.append(el)
    return changed
