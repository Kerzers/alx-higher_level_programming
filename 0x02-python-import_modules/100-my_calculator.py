#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys
argv = sys.argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = {'+': add, '-': sub, '*': mul, '/': div}
    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, op[argv[2]](a, b)))
