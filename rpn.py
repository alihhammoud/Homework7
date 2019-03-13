#!/usr/bin/env python3

import operator
import readline
import math
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            resultpow = arg1**arg2
            resultpow2 = arg2**arg1
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        RED = '\033[0m'
        print("Result: ", result)
        print("Result in radians: ", math.radians(result))

if __name__ == '__main__':
    main()

if random.randint(0,10) == 5:
    print("We did it");
