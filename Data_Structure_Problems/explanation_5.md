# Explantion of Blockchain Problem

### Code Design

Blockchain consists of a chain of block, one block's previous hash point to the hash value of previous block. This is a singly linked list problem.

### Time Complexity Analysis

Adding new Node to a singly linked list is usually O(n), since I used end pointer that point to the end of block, so time complexity of adding new block is O(1)

Printing the blockchain used recursion to retrieve the head Node, to get to the head Node, the pointer needs to go from end to head, which is O(n) time complexity

### Space Complexity Analysis

Adding one new block chain takes O(1) space
