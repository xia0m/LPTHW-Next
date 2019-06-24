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
    pivot_index = find_pivot(input_list, left, right)
    if pivot_index == -1:
        return search_helper(input_list, number, left, right)
    if input_list[pivot_index] == number:
        return pivot_index
    if input_list[left] <= number:
        return search_helper(input_list, number, left, pivot_index-1)
    else:
        return search_helper(input_list, number, pivot_index+1, right)


def find_pivot(arr, left, right):
    # the list is ordered and there is no pivot index
    if left > right:
        return -1
    # only one element left in the list
    if left == right:
        return left
    middle = left + (right-left)//2

    # compare the middle with middle +1 to find the pivot point
    if middle < right and arr[middle] > arr[middle+1]:
        return middle

    # compare the middle with middle-1 to find pivot point
    if middle > left and arr[middle] < arr[middle-1]:
        return middle-1
    # if pivot point is not found, check either left portion or right portion
    if arr[left] >= arr[middle]:
        return find_pivot(arr, left, middle-1)
    return find_pivot(arr, middle+1, right)


def search_helper(arr, target, left, right):
    # binary search
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


# Test Case 1 - normal
print("Test Case 1")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test Case 2 - Empty List
print("Test Case 2")
test_function([[], 6])

# Test Case 3 - negative Input
print("Test Case 3")
test_function([[-5, -4, -3, -2, -1, -8, -7, -6], 1])
test_function([[-5, -4, -3, -2, -1, -8, -7, -6], -8])
