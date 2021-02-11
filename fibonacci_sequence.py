'''We're going to take a look at recursion with a famous example—the Fibonacci Sequence.

The Fibonacci Sequence follows one rule: get the next number in the sequence by adding the two 
previous numbers. Here is an example of the sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
Step through each value. You start with 0 and 1. 0 + 1 = 1, so you add 1 to the sequence. 
1 + 1 = 2, so 2 is added. 1 + 2 = 3, so 3. 2 + 3 = 5, et cetera.'''

# We can generate this sequence using an iterative method (with loops):

# function get_fib(position) {
#     if (position == 0) {return 0;}
#     if (position == 1) {return 1;}

#     var first = 0,
#         second = 1,
#         next = first + second;

#     for (var i = 2, i < position; i++){
#         first = second;
#         second = next;
#         next = first + second;
#     }
#     return next;
# }


def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
