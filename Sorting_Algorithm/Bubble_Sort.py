wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22,
                13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


def bubble_sort_1(l):
    # TODO: Implement bubble sort solution
    for index in range(len(l)-1, -1, -1):
        for inner_index in range(0, index):
            if l[inner_index] > l[inner_index+1]:
                temp = l[inner_index]
                l[inner_index] = l[inner_index+1]
                l[inner_index+1] = temp


bubble_sort_1(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20),
               (22, 5), (24, 23), (21, 58), (24, 3)]


# lateste to earliest


def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    for index in range(len(l)-1, -1, -1):
        for inner_index in range(0, index):
            if l[inner_index] < l[inner_index+1]:
                temp = l[inner_index]
                l[inner_index] = l[inner_index+1]
                l[inner_index+1] = temp


print(sleep_times)
print("Pass" if (sleep_times == [
      (24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")
