#!/usr/bin/python3
""" Read file module """


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout

    Arguments:
            filename(text): name of file
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
