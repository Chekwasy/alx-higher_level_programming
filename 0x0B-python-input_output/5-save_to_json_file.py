#!/usr/bin/python3
"""json from stuff"""
import json


def save_to_json_file(my_obj, filename):
    """The j function"""

    jstuff = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as a_file:
        nb = a_file.write(jstuff)
    return (nb)
