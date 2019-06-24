import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)
    min = float('inf')
    max = float('-inf')
    for num in ints:
        if num > max:
            max = num
        if num < min:
            min = num
    return (min, max)
    # Example Test Case of Ten Integers


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# Test Case 1 - Normal Case
print("Test Case 1")
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
arr1 = [1, 3, 5, 7, 9]
print("Pass" if ((1, 9) == get_min_max(arr1)) else "Fail")

# Test Case 2 _ Empty list
print("Test Case 2")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")

# Test Case 3- Large Input List

arr2 = [i for i in range(0, 100001)]  # a list containing 0 - 9
random.shuffle(l)

print("Test Case 3")
print("Pass" if ((0, 100000) == get_min_max(arr2)) else "Fail")
