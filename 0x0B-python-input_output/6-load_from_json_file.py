#!/usr/bin/python3
"""load from a file via json"""
import json


def load_from_json_file(filename):
    """the func"""

    with open(filename, "r", encoding="utf-8") as file1:
        txt = file1.read()
        return json.loads(txt)
