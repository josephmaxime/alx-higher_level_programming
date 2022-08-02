#!/usr/bin/python3
""" JSON module """
import json


def from_json_string(my_str):
    """function that returns an objet (strin) from json representation """

    return json.loads(my_str)
