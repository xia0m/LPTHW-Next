# Longest Palindromic Subsequence


def lps(input_string):

    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    revere_string = input_string[::-1]
    loopup_matrix = [[0]*(len(input_string)+1)
                     for _ in range(len(input_string)+1)]
    max = -1
    for i in range(len(input_string)):
        for j in range(len(input_string)):
            if input_string[i] == revere_string[j]:
                if i > 0 and j > 0:
                    loopup_matrix[i][j] += loopup_matrix[i-1][j-1] + 1
                else:
                    loopup_matrix[i][j] += 1

                if loopup_matrix[i][j] > max:
                    max = loopup_matrix[i][j]

    return max


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
