#!/usr/bin/python3
import json
"""Class Base - the base for all subsequent classes"""


class Base:
    """
    Class Base - 6 func - __init__, to_json_string, save_t_file,
    from_json_string, create, load_from_file
    """
    __nb_objects = 0  # counter number of objects initialized

    def __init__(self, id=None):
        """
        func - __init__ - args - id=None - id = __nb_objects or public instance
        attribute
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
            Base.__nb_objects -= 1
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static func - args - list_dictionaries - a list of dictionaries
        returns the JSON string representation of list_dictionaries type(str)
        """
        l = []
        if list_dictionaries is None or list_dictionaries is "":
            return l
        else:
            js_str = json.dumps(list_dictionaries)
            return js_str

    @classmethod
    def save_to_file(cls, list_objs):
        """classmethod- save_to_file- args- list_objs- """
        l = []
        if list_objs is None or list_objs is "":
            with open("{}.json".format(cls.__name__), mode='w') as a_file:
                json.dump(l, a_file)
        else:
            for ob in list_objs:
                l.append(ob.to_dictionary())
            l = cls.to_json_string(l)
            with open("{}.json".format(cls.__name__), mode='w') as a_file:
                a_file.write(l)

    @staticmethod
    def from_json_string(json_string):
        """static func from_json_string - args - json_string"""
        l = []
        if json_string is None or json_string is "":
            return l
        else:
            l = json.loads(json_string)
            return l

    @classmethod
    def create(cls, **dictionary):
        """class func create - args - dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method load_from_file - no args"""
        l = []
        file = "{}.json".format(cls.__name__)
        if not file:
            return l
        else:
            with open(file) as a_file:
                l = cls.from_json_string(a_file.read())
            for x in l:
                print(x)
                print(l)
            return [cls.create(**x) for x in l]
