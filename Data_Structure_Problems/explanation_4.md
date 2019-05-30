# Explantion of Active Directory Problem

### Code Design

Each parent group may contains users list and sub-group, same for the sub-group and sub-sub-group... This problem can be seen as DFS
search problem, the parent is the root of tree, each user is leaf, each sub group is one branch. DFS search can
be implemented using recusrive function.

### Time Complexity Analysis

For the best case scenario, there is only one 1 user, 1 group, the time complexity is O(1). For the worst case scenario, we will go througth each user once, the time complexity is O(n). The average case scenario is O(n)

### Space Complexity Analysis

Since we are searching in existing group structure, no extra space is needed. space complexity is O(1)
