def Mergesort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2

    left = Mergesort(arr[:middle])
    right = Mergesort(arr[middle:])

    return merge(left, right)


def merge(left, right):

    merged_arr = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_arr.append(left[left_index])
            left_index += 1
        else:
            merged_arr.append(right[right_index])
            right_index += 1
    merged_arr += left[left_index:]
    merged_arr += right[right_index:]
    return merged_arr


test = [5, 3, 2, 4, 1]

print(Mergesort(test))
