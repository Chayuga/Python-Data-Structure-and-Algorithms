"""
1. Write a function in python that can reverse a string using stack data structure. 
Use Stack class from the tutorial."""

# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
from collections import deque


class Stack(object):

    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.conatiner) == 0

    def size(self):
        return len(self.container)


# str is the variable string
def reverse_string(str):
    stack = Stack()

    # char stands for a single character in a string
    for char in str:
        stack.push(char)

    # rstr stands for reversed_string in this context
    rstr = ''
    while stack.size() != 0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
