#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
ch = "Last digit of"
last_digit = number % 10

if last_digit > 5:
    print("{} {} is {} and is greater than 5".format(ch, number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{} {} is {} and is less than 6 and not 0".format(ch, number, last_digit))
else:
    print("{} {} is {} and is 0".format(ch, number, last_digit))
