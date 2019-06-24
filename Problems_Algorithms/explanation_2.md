# Explantion of search in a rotated sorted array

### Code Design

    This problem can be seen as a binary search problem with some extra steps. We need to find the pivot point that divide the list into two portions. Once we find the pivot point,we can compare the left most element with number to determine which portions the binary search goes into, then do binary search on correspoding portion.

### Time Complexity Analysis

    This problem can be seen as binary search problem, to find the pivot index, it takes O(log n) time, and to find the correct in binary search tree, it takes O(log n) time,so the time complexity is O(2* log n) which is still O(log n).

### Space Complexity Analysis

    The function does not require extra space except some temporary variables. Its size stay the same as the number n grow bigger, so the space complexity is O(1)
