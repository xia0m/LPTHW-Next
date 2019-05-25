# Explantion to LRU Cache Problem

### Code Design

Given the requirement that all operations must take O(1) time, my immdiate reaction was to use dictionary (HashMap). The problem of using dictionary is that it is hard to track which item
is the least recently used one. To solve this problem, Queue(implemented using Doubly Linked List) is a good choice, the least used item gets pushed in first, and gets poped first if not used.

However, adding an item in Dllist is O(1), deleting an item in Dllist is O(n) time(if we don't know the position of item). If we know the postion of a node, time complexity of deleting a node in Dllist is O(1). Therefore, we can store all the Dllist Node in a dictionary, all operation will have O(1) time.

### Complexity Analysis

Adding, deleting or getting an item in Dictionary is O(1) time. We are using Queue(Dllist) to track the order. Since we stored all node position in Dictionary, adding, deleting and getting an item is also O(1). Therefore, we get O(1) for all operation.
