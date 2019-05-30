# Explantion of File Recursion Problem

### Code Design

Each directory may contains files and sub-directory, same for the sub-directory and sub-sub-directory... This problem can be seen as DFS
search problem, the main directory is the root of tree, each file is leaf, each sub directory is one branch. DFS search can
be implemented using recusrive function.

### Time Complexity Analysis

For the best case scenario, there is only one 1 file, the time complexity is O(1). For the worst case scenario, we will go through each node once, the time complexity is O(n). The average case scenario is O(n)

### Space Complexity Analysis

One extra list to store the path info, space complexity is O(n)
