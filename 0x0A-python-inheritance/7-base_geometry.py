#!/usr/bin/python3
""" base geometry module"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
       """ Area if shape """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
       """ Validate value """

       self.name = name

       if type(value) is int:
           raise TypeError(""value" must be an integer")

       if value <= 0:
           raise ValueError(""value" must be greater than 0")

       self.value = value
