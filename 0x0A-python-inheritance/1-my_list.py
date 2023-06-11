#!/usr/bin/python3
"""my list class"""


class MyList(list):
    """class begins"""

    def __init__(self):
        """intailizati"""

        super().__init__()

    def print_sorted(self):
        """to print sorted list"""

        my = []
        my = self.copy()
        my.sort()
        print(my)
