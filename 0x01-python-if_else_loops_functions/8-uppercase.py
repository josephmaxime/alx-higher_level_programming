#!/usr/bin/python3

def uppercase(str):
    ch_up = ""

    for i in range(len(str)):

        if ((ord(str[i]) > 96) and (ord(str[i]) < 123)):
            ch = ord(str[i]) - 32
            ch_up += chr(ch) 

        else:
            ch_up += str[i]

    print("{}".format(ch_up))
