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

    def area(self):
        """ Area value of the rectangle """

        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the square with the character #
        if size is equal to 0, print an empty line.

        """
        ss_w = self.__width
        ss_h = self.__height

        for i in range(ss_h):

            for j in range(ss_w):

                print("#", end="")

            print()

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,

                                                                 self.__x,

                                                                 self.__y,

                                                                 self.__width,

                                                                 self.__height)
