# IMPLEMENT STACK USING LIST

stack = []  # the stack is equal to an empty list

# puth in stack is equal to append


def push():
    # check if stack is full
    if len(stack) == maxElem:
        print("list is full")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)


def pop_element():
    if not stack:
        print("stack is empty")
    else:
        elem = stack.pop()
        print("removed element: ", elem)
        print(stack)


while True:
    # set max element
    maxElem = input("Enter the number of elements you want in the stack: ")
    print("Select the operation 1. Push, 2. Pop, 3. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation!")
