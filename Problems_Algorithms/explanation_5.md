# Explantion of auto complete trie

### Code Design

    Trie node is like a tree structure with multiple children and multiple leaf. Each node of tree represents one letter of the word.

### Time Complexity Analysis

    Insert a new node takes O(n) time.
    Finding the prefix of a word takes O(n) time.
    Finding the suffixes is DFS search problem, it takes O(V) time,  V is the number of node.

### Space Complexity Analysis

    The space need grow as n grows, so it is O(n)
