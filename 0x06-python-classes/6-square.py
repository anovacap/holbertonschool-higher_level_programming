#!/usr/bin/python3
class Square:
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        sq_area = self.__size ** 2
        return sq_area

    def my_print(self):
        a, b = self.__position
        if self.__size is 0:
            print("")
            return
        for i in range(b):
            print("")
        for i in range(self.__size):
            print("{}{}".format(a * " ", self.__size * "#"),  end="")
            print("")
