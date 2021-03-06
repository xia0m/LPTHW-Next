# Your solution
def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    steps = 0
    if target == 0:
        return 0
    while target != 0:
        if target % 2 == 0:
            target = target/2
            steps += 1
        else:
            target = target - 1
            steps += 1
    return steps

# Test Cases


def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)

target = 69
solution = 9
test_case = [target, solution]
test_function(test_case)
