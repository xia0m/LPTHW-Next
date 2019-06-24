# Explantion of square root

### Code Design

    The integer can be seen as a long list consists of integers from 0 to n. Finding the square root of that number is then a binary search problem, where the stop condition is the difference of n/sqrt - floor(sqrt) between 0 and 1

### Time Complexity Analysis

    This problem can be seen as binary search problem, each time the list is cut by half, so it is O(log n)

### Space Complexity Analysis

    The function does not require extra space except some temporary variables. Its size stay the same as the number n grow bigger, so the space complexity is O(1)
