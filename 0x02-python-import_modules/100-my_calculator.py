#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == '__main__':

    from sys import argv

    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:

        operators = argv[2]

        if operators == "+":
            print("{} {} {} = {}".format(int(argv[1]), operators, int(argv[3]),
                                         add(int(argv[1]), int(argv[3]))))
        elif operators == "-":
            print("{} {} {} = {}".format(int(argv[1]), operators, int(argv[3]),
                                         sub(int(argv[1]), int(argv[3]))))
        elif operators == "*":
            print("{} {} {} = {}".format(int(argv[1]), operators, int(argv[3]),
                                         mul(int(argv[1]), int(argv[3]))))
        elif operators == "/":
            print("{} {} {} = {}".format(int(argv[1]), operators, int(argv[3]),
                                         div(int(argv[1]), int(argv[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
