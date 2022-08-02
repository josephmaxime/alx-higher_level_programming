#!/usr/bin/python3
""" JSON module """
from sys import argv
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":

    try:
        obj_ = load_from_json_file("add_item.json")
    except Exception:
        obj_ = []

    length = len(argv)
    for i in range(1, length):
        obj_.append(argv[i])

    save_to_json_file(obj_, "add_item.json")
