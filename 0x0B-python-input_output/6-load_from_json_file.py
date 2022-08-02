#!/usr/bin/python3
""" JSON module """
import json


def load_from_json_file(filename):
    """function that create an objet (string)
    from json representation file
    """

    with open(filename, 'r', encoding="utf-8") as f:

        obj_ = json.load(f)

    return obj_
