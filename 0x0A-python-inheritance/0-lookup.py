#!/usr/bin/python3
""" 0-lookup module"""


def lookup(obj):
    """function: list of available attributes and methods of an object."""

    return [objet for objet in dir(obj)]
