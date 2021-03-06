#!/usr/bin/python3
"""Defines class Square(Rectangle) 6 functions"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square - parent class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """func __init__ - args - size, x=0, y=0, id=None"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """func __str__ - no args"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """func width getter"""

        return self.width

    @size.setter
    def size(self, value):
        """func width setter - args - value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """func update - args - *args, **kwargs"""
        if args:
            for i, arg in enumerate(args):
                if i is 0:
                    self.id = args[0]
                if i is 1:
                    self.size = args[1]
                elif i is 2:
                    self.x = args[2]
                elif i is 3:
                    self.y = args[3]
        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """func to_dictionar - no arg"""
        d = {}
        d['id'] = self.id
        d['size'] = self.size
        d['x'] = self.x
        d['y'] = self.y
        return d
