def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(input_list)-1
    middle = right//2

    # if the target number is less than the right most number, that means it is within the right portion
    # of the array, we just need to find the start index of right portion, then do a binary search

    if number <= input_list[right]:
        while number <= input_list[middle]:
            middle = middle//2
        return search_helper(input_list, number, middle, right)

    # if the target number is greater than the left most number, that means it is within the left portion
    # of the array, we just need to find the end index of left portion, then do a binary search
    elif number >= input_list[left]:
        while number >= input_list[middle]:
            middle = middle + (right-middle)//2
        return search_helper(input_list, number, left, middle)
    # if the target number is less than the left most number, greater than the right most number, that
    # means its not in the input list, return -1
    else:
        return -1

    return search_helper(input_list, number, 0, len(input_list)-1)


def search_helper(arr, target, left, right):

    if left > right:
        return -1
    middle = left + (right-left)//2
    if target == arr[middle]:
        return middle
    elif target < arr[middle]:
        return search_helper(arr, target, left, middle-1)
    else:
        return search_helper(arr, target, middle+1, right)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
