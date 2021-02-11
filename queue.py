# Working with lists
from collections import deque
mog = ['Mary', 'John', 'Susan']
print(mog)

mog.pop()
print(mog)


deque(['q', 'd', 'r', 'y'])
print(deque())

# Adding or removing elements from a linked list.
llist = deque("abcde")
print(llist)

llist.append("f")
print(llist)

# Using Deque to add or remove element from left side, or head , of the list
llist.appendleft("z")
print(llist)


popped = llist.popleft()
print(popped)


"""Implementing Deque in Queues."""


queue = deque()
print(queue)

queue.append("Mary")
queue.append("John")
queue.append("Susan")

print(queue)

# Removing elements form queue

print(queue.popleft())

"""Implementing Deque in Stacks.
This uses LIFO approach"""


history = deque()

history.appendleft('Chayuga')
history.appendleft('Senaji')
history.appendleft('Rodgers')
history.append("Family")

print(history)

# Remove element
history.popleft()
history.popleft()
history.pop()

print(history)
