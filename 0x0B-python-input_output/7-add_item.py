#!/usr/bin/python3
"""fun to save all arguments"""
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
from sys import argv
import os


if not os.path.exists("add_item.json"):
    lst = []
else:
    lst = load_from_json_file("add_item.json")
if len(argv) > 1:
    for a in range(len(argv)):
        if a > 1:
            lst.append(argv[a])

save_to_json_file(lst, "add_item.json")
