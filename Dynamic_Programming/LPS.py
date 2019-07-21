# Longest Palindromic Subsequence


def lps(input_string):

    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    pass


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)


string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)


string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)
