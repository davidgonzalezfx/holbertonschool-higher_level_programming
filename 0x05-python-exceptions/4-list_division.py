#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_division = []
    for idx in range(list_length):
        try:
            el = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print('division by 0')
            el = 0
        except TypeError:
            print('wrong type')
            el = 0
        except IndexError:
            print('out of range')
            el = 0
        finally:
            res_division.append(el)
    return res_division
