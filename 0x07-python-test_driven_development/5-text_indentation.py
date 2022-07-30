#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    space = 0

    for letter in text:

        if space == 0:

            if letter == ' ':
                continue

            else:
                space = 1

        if space == 1:

            if letter == '?' or letter == '.' or letter == ':':
                print(letter)
                print()

                space = 0

            else:
                print(letter, end="")
