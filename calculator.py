"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    split_number = user_input.split(" ")
    num1 = int(split_number[1])
    num2 = int(split_number[2])
    if split_number[0] == "+":
        print add(num1, num2)
    elif split_number[0] == "-":
        print subtract(num1, num2)
    elif split_number[0] == "*":
        print multiply(num1, num2)
    elif split_number[0] == "/":
        print divide(num1, num2)
    elif split_number[0] == "square":
        print square(num1)
    elif split_number[0] == "cube":
        print cube(num1)
    elif split_number[0] == "pow":
        print power(num1, num2)
    elif split_number[0] == "%":
        print mod(num1, num2)
    else:
        print "This is not an operator."