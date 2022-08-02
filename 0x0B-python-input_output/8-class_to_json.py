#!/usr/bin/python3
""" Class to JSON module
"""
#to_j_s = import('3-to_json_string.py').to_json_string


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure for json serialisation"""

    obj_ = (obj.__dict__)

    return obj_
