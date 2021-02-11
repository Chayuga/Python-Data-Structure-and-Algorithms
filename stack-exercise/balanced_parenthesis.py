"""
Write a function in python that checks if paranthesis in the string are balanced or not.
Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial."""
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True


# SOLUTION ONE:
from collections import deque


class Stack(object):
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.comtainer[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


"""# Match characters to it's equivalent.


def is_match(char1, char2):
    match_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    return match_dict[char1] == char2

# Check if the parenthesis are balanced
# str is the string to be checked for a balanced parenthesis
def is_balanced(str):
    stack = Stack()

    # Check for parenthesis in the string given
    for char in str:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char == ']':
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False

    return stack.size() == 0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("({[]})"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
"""


# SOLUTION TWO:


def is_match(parenth1, parenth2):
    if parenth1 == '(' and parenth2 == ')':
        return True

    elif parenth1 == '{' and parenth2 == '}':
        return True

    elif parenth1 == '[' and parenth2 == ']':
        return True

    else:
        return False


def is_parenth_balanced(parenth_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parenth_string) and is_balanced:
        parenth = parenth_string[index]
        if parenth in "([{":
            s.push(parenth)

        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parenth):
                    is_balanced = False

            index += 1

    if s.is_empty() and is_balanced:
        return True

    else:
        return False



print(is_parenth_balanced("({a+b})"))
print(is_parenth_balanced("))((a+b}{"))
print(is_parenth_balanced("((a+b))"))
print(is_parenth_balanced("((a+g))"))
print(is_parenth_balanced("))"))
print(is_parenth_balanced("({[]})"))
print(is_parenth_balanced("[a+b]*(x+2y)*{gg+kk}"))
