#!/usr/bin/python3


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        func - __init__ - args - id=None
        """
        self.id = id
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
            Base.__nb_objects -= 1
        else:
            self.id = Base.__nb_objects
