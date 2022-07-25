#!/usr/bin/python3
"""Module to define rectangle"""


class Rectangle:
    """Define class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1

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

        if (len_w == 0) or (len_h == 0):
            return str_

        for j in range(len_h):

            for i in range(len_w):
                str_ += str(self.print_symbol)

            if (j < len_h - 1):
                str_ += "\n"

        return str_

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method."""

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        elif rect_1.area() < rect_2.area():
            return rect_2

        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Class method to create a square."""

        return cls(size, size)
