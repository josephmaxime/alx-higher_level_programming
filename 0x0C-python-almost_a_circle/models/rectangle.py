#!/usr/bin/python3
"""Module Rectangle models """
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize paramater"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Retreive widt attribute of rectangle """
        return self.__width

    @property
    def height(self):
        """ Retreive heigh attribute of rectangle """
        return self.__height

    @property
    def x(self):
        """Retreive x attribute of rectangle """
        return self.__x

    @property
    def y(self):
        """Retreive y attribute of rectangle """
        return self.__y

    @width.setter
    def width(self, value):
        """set value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """set value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """set value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """set value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
