#!/usr/bin/python3
"""Insert line to a file module """


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string"""

    with open(filename, 'r', encoding="utf-8") as f:

        lines = f.readlines()
        text = ""

        for line in lines:

            text += line
            if line.find(search_string) != -1:

                text += new_string

    with open(filename, 'w', encoding="utf-8") as f:

        write_file = f.write(text)
