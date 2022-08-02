#!/usr/bin/python3
"""Add text to a file module """


def append_write(filename="", text=""):
    """function that add a string to a text file (UTF8)
    and returns the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        write_file = f.write(text)

    return write_file
