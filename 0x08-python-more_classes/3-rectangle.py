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
        """Retreive width attribute of rectangle"""
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
                self.__width = value

    @property
    def height(self):
        """Retreive height attribute of rectangle"""
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

    def area(self):
        """Area of rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of rectangle"""

        if (self.__width == 0) or (self.__height == 0):
            return 0

        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """print the rectangle with the character #."""

        str_ = ""
        len_w = self.__width
        len_h = self.__height

        if (len_w == 0) and (len_h == 0):
            return ""

        else:
            for j in range(len_h):

                for i in range(len_w):
                    str_ += "#"

                str_ += "\n"
            return str_
