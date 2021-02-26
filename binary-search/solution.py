"""
Binary Search Exercise
When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

numbers = [1,4,6,9,10,5,7]

Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  
This should return 5,6,7 as indices containing number 15 in the array
"""


def binary_search(numbers, number_to_find):
    left_index = 0
    right_index = len(numbers) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1

        else:  # number to find is on left hand side of the list
            right_index = mid_index - 1

    return -1


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]

    # find indices on left hand side
    i = index - 1

    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)

        else:
            break
        i = i - 1

    # find indices on the right hand side
    i = index + 1

    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
