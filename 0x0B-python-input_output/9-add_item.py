#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    py_l = load_from_json_file('add_item.json')
except:
    py_l = []

for i in range(1, len(argv)):
    py_l.append(argv[i])
save_to_json_file(py_l, 'add_item.json')
