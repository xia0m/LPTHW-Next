def sort_012(input_list):
    left = 0
    right = len(input_list) - 1

    i = 0
    while i <= right:
        if input_list[i] == 0:
            input_list[i] = input_list[left]
            input_list[left] = 0
            left += 1
            i += 1
        elif input_list[i] == 2:
            input_list[i] = input_list[right]
            input_list[right] = 2
            right -= 1
        else:
            i += 1


def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
