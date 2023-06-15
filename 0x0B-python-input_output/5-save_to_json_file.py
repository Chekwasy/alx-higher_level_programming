#!/usr/bin/python3
"""json from stuff"""
import json


def save_to_json_file(my_obj, filename):
    """The j function"""

    with open(filename, 'w') as a_file:
        json.dump(my_obj, a_file)
