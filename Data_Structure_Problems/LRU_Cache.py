class DoublyLinkedList:
    def __init__(self, value, prev, next):
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
            self.add_to_end(key)
            self.remove_from_list(key)
            return self.cache_dict[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item
        if self.filled_cache < self.cache_size:
            self.cache_dict[key] = value
            self.add_to_end(key)
            self.filled_cache += 1
        else:
            if key in self.cache_dict:
                self.add_to_end(key)
                self.remove_from_list(key)
            else:
                self.add_to_end(key)
                item_key = self.pop_front()
                del self.cache_dict[item_key]
            self.cache_dict[key] = value

    def add_to_end(self, key):
        if self.head is None or self.tail is None:
            self.head = DoublyLinkedList(key, None, None)
            self.tail = self.head
            return
        temp = self.tail
        self.tail = DoublyLinkedList(key, self.tail, None)
        temp.next = self.tail

    def remove_from_list(self, key):
        pass

    def pop_front(self):
        return ''


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
print(our_cache.cache_dict)
print(our_cache.head.next.value)
print(our_cache.tail.prev.value)
# print(our_cache.get(1))
# print(our_cache.get(2))
# print(our_cache.get(3))
