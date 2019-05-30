# Explantion of Huffman Coding

### Code Design

Given a list, to determine each relevant frequencies of a character, I used dictionary. Dictionary does not allow duplicate keys, and if a duplicate keys is found, the frequency gets added to the corresponding key.
I stored frequency,key pair in a list of tuples. List is ordered data structure, it's is to be sorted.
To build a tree, I used binary tree. Each Node consists of two edges.
To generate the binary encoded value, I used recursion. To determine the path of specific Node, I used DFS search, which can be implemented using recursion.

### Time Complexity Analysis

count frequency of characters: O(n) , go over a list size of N
tuple*list: O(n), go over a list of size N
build_huffman_tree: O(n^2 * logn), the while loop takes O(n), to append an item to a list is O(n), to sort a list, the time complexity is O(n^2 \*logn), so the time complexity is O(n^2 logn)
get_binary_value:O(V+E), DFS search, V is the total vertice of the tree, E is the total edge of the
huffman_decoding: O(n), go through a list of items.

### Space Complexity Analysis

O(n) to build the tree, O(n) for list of tuples, O(n) for the dictionary.
