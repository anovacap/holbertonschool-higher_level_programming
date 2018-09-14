#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    arg = sys.argv
    operators = {'+', '-', '*', '/'}
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif arg[2] in operators:
        if arg[2] == "+":
            print("{} + {} = {}".format(arg[1], arg[3], calculator_1.add
                                        (int(arg[1]), int(arg[3]))))
        if arg[2] == "-":
            print("{} - {} = {}".format(arg[1], arg[3], calculator_1.sub
                                        (int(arg[1]), int(arg[3]))))
        if arg[2] == "*":
            print("{} * {} = {}".format(arg[1], arg[3], calculator_1.mul
                                        (int(arg[1]), int(arg[3]))))
        if arg[2] == "/":
            print("{} / {} = {}".format(arg[1], arg[3], calculator_1.div
                                        (int(arg[1]), int(arg[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
