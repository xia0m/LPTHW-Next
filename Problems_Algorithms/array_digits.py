def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        raise Exception("at least two number is needed")
    if input_list is None:
        raise Exception("Input cannot be None")

    new_list = reverse_merge_sort(input_list)

    left_num = get_number(new_list, 0)
    right_num = get_number(new_list, 1)

    return left_num, right_num


def get_number(arr, start_index):
    step = 2
    result = ''
    for x in range(start_index, len(arr), step):
        result += str(arr[x])
    return int(result)


def reverse_merge_sort(arr):

    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = reverse_merge_sort(arr[:middle])
    right = reverse_merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    new_arr = []

    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            new_arr.append(left[left_index])
            left_index += 1
        else:
            new_arr.append(right[right_index])
            right_index += 1

    new_arr += left[left_index:]
    new_arr += right[right_index:]

    return new_arr


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test Case 1 - Normal Input
print("Test Case 1")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# Test Case 2 - Empty list, Null input
print("Test Case 2")
try:
    test_function([[1], [1, None]])
except Exception:
    print("At least two number is needed")

try:
    test_function([None, [1, None]])
except Exception:
    print("Input cannot be None")

# Test Case 3 - only 2 number, list of same number
print("Test Case 3")
test_function([[1, 2], [2, 1]])
test_function([[1, 1, 1, 1, 1, 1], [111, 111]])
