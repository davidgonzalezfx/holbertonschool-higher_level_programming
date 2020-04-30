#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    names_list = dir(hidden_4)
    for name in names_list:
        if name[:2] != '__':
            print(name)
