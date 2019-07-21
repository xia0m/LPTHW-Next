# the coin change problem


def coin_change(coins, amount):

    # TODO: Complete the coin_change function
    # This should return one value: the fewest coins needed to make up the given amount
    smallest = -1
    temp = amount
    for _ in range(len(coins)):
        count = 0
        temp = amount
        while temp > 0:
            if temp < coins[0]:
                break
            for coin in reversed(coins):
                if temp >= coin:
                    temp -= coin
                    count += 1
                    break

        if temp == 0:
            if smallest == -1:
                smallest = count
            if smallest > count:
                smallest = count
    return smallest


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)


arr = [1, 4, 5, 6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5, 7, 8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)