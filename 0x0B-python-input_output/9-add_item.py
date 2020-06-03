#!/usr/bin/python3
'''
file: 9-add_item.py
description: adds all arguments to a Python list, and then save them to a file
'''
from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

arg_list = []
if path.isfile(filename):
    arg_list = load_from_json_file(filename)

for a in argv[1:]:
    arg_list.append(a)

save_to_json_file(arg_list, "add_item.json")
