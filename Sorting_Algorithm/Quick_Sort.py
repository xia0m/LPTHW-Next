def quick_sort(arr):

    quick_sort_helper(arr, 0, len(arr)-1)


def quick_sort_helper(arr, left, right):
    if left > right:
        return
    pivot_index = right
    pivot_value = arr[pivot_index]

    while(left != pivot_index):
        if arr[left] <= pivot_value:
            left += 1
            continue
        arr[pivot_index] = arr[left]
        pivot_index -= 1
        arr[left] = arr[pivot_index]
        arr[pivot_index] = pivot_value
    quick_sort_helper(arr, 0, left-1)
    quick_sort_helper(arr, left+1, right)


arr = [8, 3, 1, 7, 0, 10, 2]
quick_sort(arr)
print(arr)
