#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square begins"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization for square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation method for square"""

        return "[Square] "+"("+str(self.id)+") "+str(self.x)+"/"+\
            str(self.y)+" - "+str(self.width)
