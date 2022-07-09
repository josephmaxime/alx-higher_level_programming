#!/usr/bin/python3

def complex_delete(my_dict, value):

    keys_del = []

    for key in my_dict:

        if my_dict[key] == value:

            keys_del.append(key)

    for key in keys_del:

        del my_dict[key]

    return my_dict
