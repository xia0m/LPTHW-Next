# Longest Common Subsequence
def lcs(string_a, string_b):
    lookup_matrix = [[0]*(len(string_a)+1) for _ in range(len(string_b)+1)]

    for i in range(0, len(string_b)):
        for j in range(i, len(string_a)):
            if string_b[i] == string_a[j]:
                max_value = max(
                    lookup_matrix[i][j+1], lookup_matrix[i+1][j], lookup_matrix[i+1][j+1]+1)
                lookup_matrix[i+1][j+1] = max_value
                for rest_row in range(i, len(lookup_matrix)):
                    for rest_column in range(j, len(lookup_matrix[rest_row])):
                        lookup_matrix[rest_row][rest_column] = max_value
                break

    return lookup_matrix[-1][-1]


test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1 == 5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2 == 7, "Incorrect LCS value."
print('Tests passed!')
