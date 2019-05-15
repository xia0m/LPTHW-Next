# # list version


def bubble_sort(a_list):
    for _ in range(len(a_list)):
        for inner_index in range(len(a_list)-1):
            if a_list[inner_index] > a_list[inner_index+1]:
                temp = a_list[inner_index]
                a_list[inner_index] = a_list[inner_index+1]
                a_list[inner_index+1] = temp


a_list = [5, 4, 3, 2, 1]
bubble_sort(a_list)
print(a_list)
