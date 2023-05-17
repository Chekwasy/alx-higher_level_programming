#!/usr/bin/python3
"""the funct"""


def append_after(filename="", search_string="", new_string=""):
    """it begins"""

    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        new_text = []

        for line in text:
            new_text.append(line)

            if search_string in line:
                new_text.append(new_string)

    with open(filename, mode='a', encoding='utf-8') as nf:
        for line in new_text:
            nf.write(line)
