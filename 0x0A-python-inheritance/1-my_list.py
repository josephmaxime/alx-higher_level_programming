#!/usr/bin/python3
""" 1-MyList module"""


class MyList(list):
    """Class that inherit from list"""

    def __init__(self):
        """Initialize list subclass list"""
        super()

    def print_sorted(self):
        """function: list of available attributes and methods of an object."""

        print(sorted(self))
