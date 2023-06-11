#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if len(sys.argv) == 4:
        if sys.argv[2] == "+":
                print("{} + {} = {} ".format(int(sys.argv[1]) ,int(sys.argv[3]), add(int (sys.argv[1]),int (sys.argv[3]))))
                sys.exit(0)
        elif sys.argv[2] == "-":
                print("{} - {} = {} ".format(int(sys.argv[1]) ,int(sys.argv[3]), sub(int (sys.argv[1]),int (sys.argv[3]))))
                sys.exit(0)
        elif sys.argv[2] == "*":
                print("{} * {} = {} ".format(int(sys.argv[1]) ,int(sys.argv[3]), mul(int (sys.argv[1]),int (sys.argv[3]))))
                sys.exit(0)
        elif sys.argv[2] == "/":
                print("{} / {} = {} ".format(int(sys.argv[1]) ,int(sys.argv[3]), div(int (sys.argv[1]),int (sys.argv[3]))))
                sys.exit(0)
        else:
            print ("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

