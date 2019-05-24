# Set up a Doubly Linked List, here DLlist works like a
# Queue, where new item added to the end of list,
# old item gets poped first


class DoublyLinkedList:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_dict = dict()
        self.cache_size = capacity
        self.filled_cache = 0
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache_dict:
            # if a node gets used, move this node to the end of queue
            value = self.cache_dict[key].value
            self.remove_from_list(key)
            self.add_to_tail(key, value)
            return self.cache_dict[key].value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item

        # if the cache is not at capacity, add the item to dictionary and
        # the DL list
        if self.filled_cache < self.cache_size:
            self.add_to_tail(key, value)
            self.filled_cache += 1
        else:
            if key in self.cache_dict:
                # if a node is used, move it to the end of queue
                self.remove_from_list(key)
                self.add_to_tail(key, value)
            else:
                # if a node is not in the list, remove the head
                # of queue and also remove it from dictionary
                # add the new node to the end of queue
                item_key = self.pop_head()
                del self.cache_dict[item_key]
                self.add_to_tail(key, value)

    def add_to_tail(self, key, value):
        # check whether the DL list is empty, if it is empty,
        # create a new DL list Node, head and taill will be point
        # to the same node
        if self.head is None:
            self.head = DoublyLinkedList(key, value, None, None)
            self.tail = self.head
            self.cache_dict[key] = self.tail
            return
        # add the item to the end of the list
        temp = self.tail
        self.tail = DoublyLinkedList(key, value, self.tail, None)
        temp.next = self.tail
        self.cache_dict[key] = self.tail

    def remove_from_list(self, key):
        node = self.cache_dict[key]
        del self.cache_dict[key]

        if self.head is None or node is None:
            return
        # if the node is at the head of Dllist
        if self.head == node:
            self.head = node.next
        # check to see if the node is last item
        if node.next is not None:
            node.next.prev = node.prev

        # check to see if the node is first node
        if node.prev is not None:
            node.prev.next = node.next

    def pop_head(self):
        if self.head is None:
            return None
        key = self.head.key
        self.head = self.head.next

        return key


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
# our_cache.set(6, 6)
# print(our_cache.cache_dict)
# print(our_cache.head.next.value)
# print(our_cache.tail.prev.value)
print(our_cache.get(1))
our_cache.set(6, 6)
print(our_cache.get(2))
our_cache.set(7, 7)
print(our_cache.get(2))
print(our_cache.get(3))
print(our_cache.get(4))

print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(3))
