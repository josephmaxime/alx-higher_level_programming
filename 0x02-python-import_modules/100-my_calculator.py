#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == '__main__':

    from sys import argv

    length = len(argv)
    operators = argv[2]

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if operators == '+':
            print("{:d} {:s} {:d} = {:d}".format(argv[1], argv[3],
                add(argv[1], argv[3])))
    elif operators == '-':
            print("{:d} {:s} {:d} = {:d}".format(argv[1], argv[3],
                sub(argv[1], argv[3])))
    elif operators == '*':
            print("{:d} {:s} {:d} = {:d}".format(argv[1], argv[3],
                mul(argv[1], argv[3])))
    elif operators == '/':
            print("{:d} {:s} {:d} = {:d}".format(argv[1], arg[3],
                div(argv[1], argv[3])))
    else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
