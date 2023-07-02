#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """represent class square"""
    def __init__(self, size=0):
        """initializ a square
        Args:
        size(int): The size of the new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size*self.__size
