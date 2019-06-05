# Binary search interatively


def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    length = len(array)
    middle = int(length/2)
    index = -1
    while middle >= 1:
        if array[middle] == target:
            return middle
        elif target > array[middle]:
            middle = int(middle/2+middle)
        elif target < array[middle]:
            middle = int(middle/2)
    return index


# def test_function(test_case):
#     answer = binary_search(test_case[0], test_case[1])
#     if answer == test_case[2]:
#         print("Pass!")
#     else:
#         print("Fail!")


# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 6
# index = 6
# test_case = [array, target, index]
# test_function(test_case)

# Recursive Solution


def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if start_index > end_index:
        return -1
    middle = int(start_index + end_index)//2
    if array[middle] == target:
        return middle
    elif target > array[middle]:
        return binary_search_recursive(array, target, middle+1, end_index)
    elif target < array[middle]:
        return binary_search_recursive(array, target, start_index, middle-1)


def test_function(test_case):
    answer = binary_search_recursive(
        test_case[0], test_case[1], 0, len(test_case[0])-1)
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)
