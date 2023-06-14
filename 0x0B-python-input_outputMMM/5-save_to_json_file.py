#!/usr/bin/python3
"""func to save json to str in a file"""
import json


def save_to_json_file(my_obj, filename):
    """d func"""

    with open(filename, "w", encoding="utf-8") as file1:
        file1.write(json.dumps(my_obj))
