def quick_sort(sequence):
    # get the length of the sequence
    length = len(sequence)

    # check corner cases, if the sequence is either one or less return the sequence
    if length <= 1:
        return sequence

    # otherwise get the pivot (last element on the list) by popping the last element
    else:
        pivot = sequence.pop()

    # Create an empty list to store elements that are greater than the pivot and another one 
    # at is less than the pivot
    items_greater = []
    items_lower = []

    # loop through the list
    for item in sequence:
        # add all the elements that are greater than the pivot to the greater than list, created above.
        if item > pivot:
            items_greater.append(item)

        # add all the elements that are less than the pivot to the less than list, created above.
        else:
            items_lower.append(item)

    # Return the list in less than list to the pivot and greater than list, to return a quick sorted list.
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


if __name__ == '__main__':
    sequence = [2, 6, 52, 1, 3, 0, 12]

    sorted = quick_sort(sequence)
    print(sorted)
   