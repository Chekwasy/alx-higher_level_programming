#!/usr/bin/python3
"""Load add and save """
from sys import argv
from os import path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if len(argv) < 2:
    if path.exists('add_item.json'):
        the_list = load_from_json_file('add_item.json')
    else:
        the_list = []
        save_to_json_file(the_list, 'add_item.json')
else:
    if path.exists('add_item.json'):
        the_list = load_from_json_file('add_item.json')
        for i in range(1, len(argv)):
            the_list.append(argv[i])
        save_to_json_file(the_list, 'add_item.json')
    else:
        the_list = []
        for i in range(1, len(argv)):
            the_list.append(argv[i])
        save_to_json_file(the_list, 'add_item.json')
