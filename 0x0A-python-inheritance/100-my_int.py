#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """Class myint begins"""

    def __eq__(self, ot):
        """eualto method"""

        return self.real != ot

    def __ne__(self, ot):
        """not equalto method"""

        return self.real == ot
