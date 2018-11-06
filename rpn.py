#!/usr/bin/env python3

import operator
import colorama
from colorama import init
init()
from colorama import Fore


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def printStuff():
    print("Hello")
    print("World")
    print("My")
    print("Name")
    print("Is")
    print("Meelan")

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
            print(token)
        except ValueError:
            print(Fore.BLUE + token)
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
