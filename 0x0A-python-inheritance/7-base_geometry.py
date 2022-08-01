#!/usr/bin/python3
""" base geometry module"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
       """ Area if shape """
       raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
       """ Validate value """

       if type(value) is not int:
           raise TypeError("{:s} must be an integer".format(name))

       if value <= 0:
           raise ValueError("{:s} must be greater than 0".format(name))
