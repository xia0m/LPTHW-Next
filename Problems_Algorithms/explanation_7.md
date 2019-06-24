# Explantion of HTTP Router

### Code Design

    Trie node is like a tree structure with multiple children and multiple leaf. Each node of tree represents one part of web address seprate by '/'.

### Time Complexity Analysis

    Insert a new node takes O(n) time.
    Spliting the path takes O(n) time.
    Finding the address takes O(n) time.

### Space Complexity Analysis

    The space need grow as n grows, so it is O(n)
