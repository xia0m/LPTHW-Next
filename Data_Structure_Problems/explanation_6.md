# Explantion of Union and Intersection Problem

### Code Design

There is no new data structure used for this problem, they are basic linked list operation.

### Time Complexity Analysis

Searching one item in linkeds cost O(n) time, and searching function (is_in_list()) is inside a while loop(go over one list), so the time complexity is O(n^2)

### Space Complexity Analysis

In the problem, I created a new linked list to store and intersection and union result, union takes O(m+n) space, intersection taks O(n) space
