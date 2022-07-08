#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dic = a_dictionary.copy()

    for key in a_dictionary.keys():
        dict_ = {key: (a_dictionary[key] * 2)}
        new_dic.update(dict_)

    return new_dic
