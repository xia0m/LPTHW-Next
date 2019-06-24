# Explantion of rearrange array elements

### Code Design

    I did a reverse merge sort first as merge sort gives guaranteed O(n * log n) time complexity. If the length of input list is odd, 0, 2i, 4i ... can be used as first number, the second number is 1, 2i+1. If the length of input list is even, the first number is 0,2i,4i, the second number is 1, 2i+1, 4i+1. Their sum is guaranteed to be maxmium.

### Time Complexity Analysis

    Mergesort the list takes O(n * log n) time.

### Space Complexity Analysis

    Since Mergesort takes one extra list, the space complexity is O(n)
