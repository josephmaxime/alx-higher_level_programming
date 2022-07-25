#!/usr/bin/python3
"""Module to define rectangle"""


class Rectangle:
    """Define class rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize attributes of rectangle

        Args:
            width (int): must be an positive integer.
            height (int): must be an positive integer.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        else:
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")

        else:
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height

    @property
    def width(self):
        """Retreive width attribute of rectangle""""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value of width rectangle attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self._width = value

    @property
    def height(self):
        """Retreive height attribute of rectangle""""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value of height rectangle attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
