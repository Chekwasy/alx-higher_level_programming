#!/usr/bin/python3
"""function to change json str to real str"""
import json


def from_json_string(my_str):
    """from json"""

    return json.loads(my_str)
