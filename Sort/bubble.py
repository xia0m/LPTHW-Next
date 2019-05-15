# list version


def bubble_sort(a_list):
    for passnum in range(len(a_list)-1, 0, -1):
        for i in range(passnum):
            if a_list[i] > a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp


a_list = [7, 4, 8, 3, 2, 3, 2, 7, 9, 2, 2, 1, 4, 8]
bubble_sort(a_list)
print(a_list)
