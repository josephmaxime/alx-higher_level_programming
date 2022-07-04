#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):

        if ((ord(str[i]) > 96) and (ord(str[i]) < 123)):
            ch = ord(str[i]) - 32
            print("{}".format(chr(ch)), end='')

        else:
            print("{}".format(str[i]), end='')
