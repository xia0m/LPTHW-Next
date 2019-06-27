def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    platforms = 0
    if len(arrival) == 0 or len(departure) == 0:
        return platforms

    start = -1
    end = 2500
    max_platforms = []

    for index in range(len(arrival)):
        if arrival[index] > start and arrival[index] < end:
            platforms += 1
        else:
            max_platforms.append(platforms)
            platforms = 1
            start = -1
            end = 2500
        if arrival[index] > start:
            start = arrival[index]
        if departure[index] < end:
            end = departure[index]
    print(max(max_platforms))
    return max(max_platforms)


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
