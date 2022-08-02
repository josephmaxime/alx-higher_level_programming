#!/usr/bin/python3
""" JSON module """
import json


def save_to_json_file(my_obj, filename):
    """function that write an objet (string)
    to a text file using json representation
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
