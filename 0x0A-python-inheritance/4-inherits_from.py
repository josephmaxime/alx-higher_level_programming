#!/usr/bin/python3
""" inherit_from module"""


def inherits_from(obj, a_class):
    """function: list of available attributes and methods of an object."""

    test = False

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        test = True

    return test
