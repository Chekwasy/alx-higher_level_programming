#!/usr/bin/python3
"""my list class"""


class MyList(list):
    """class begins"""

    def print_sorted(self):
        """to print sorted list"""

        my = []
        my = self.copy()
        my.sort()
        print(my)
