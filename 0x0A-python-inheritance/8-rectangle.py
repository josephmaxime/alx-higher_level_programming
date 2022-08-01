#!/usr/bin/python3
""" base geometry module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherite BaseGeometry class"""

    def __init__(self, width, height):
       """Initialize attributes"""

       self.integer_validator("width", width)
       self.__width = width

       self.integer_validator("height", height)
       self.__height = height
