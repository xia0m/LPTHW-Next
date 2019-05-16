def deep_reverse(arr):
    result = []
    if len(arr) > 0:
        if type(arr[-1]) is not list:
            result += ([arr[-1]] + deep_reverse(arr[:-1]))
        else:
            result.append(deep_reverse(arr[-1]))
            result += deep_reverse(arr[:-1])
    return result


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3], 4, [5, 6]]
solution = [[6, 5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)
