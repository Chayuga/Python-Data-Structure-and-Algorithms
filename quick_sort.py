"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    if len(array) > 1:
        pivot = array[len(array)-1]
        left, mid, right = [], [], []
        for i in range(len(array)-1):
            if array[i] < pivot:
                left.append(array[i])
            elif array[i] > pivot:
                right.append(array[i])
            else:
                mid.append(array[i])
        mid.append(pivot)
        return quicksort(left) + mid + quicksort(right)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
