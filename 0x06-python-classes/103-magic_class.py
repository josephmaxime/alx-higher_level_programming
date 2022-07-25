#!/usr/bin/python3
""" Magic calculator radius module"""
import math

class MagicClass:
    """This class define a cyrcle"""

    def __init__(self, radius=0):
        """Initialize variable"""
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area of a cycle."""
        return (self.__radius ** 2) * (math.pi)

    def circumference(self):
        """Circumference of cycle."""
        return 2 * (math.pi) * (self.__radius)
