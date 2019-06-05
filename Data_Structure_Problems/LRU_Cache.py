# Set up a Doubly Linked List, here DLlist works like a
# Queue, where new item added to the end of list,
# old item gets poped first


class DoublyLinkedList:
    def __init__(self, key, value, prev, next):
        """
        The class for Doulby Linked List
        ...
        Attributes
        ...........
        key: int or str
            a key for the value store in dllist
        value: 
            the value needs to be stored in dllist
        prev: object
            pointer point to previous Node
        next: object
            pointer point to next NOde
        """

        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRU_Cache(object):
    """
    The class for least recently used cache
    ...
    Attributes
    ...........
    cache_dict: dict
        a dictionary to store key,dllist Node pair
    cache_size: int
        the max capacity of a cache
    filled_cache: int
        number of itme in cache
    head: object
        pointer point to the head of dllist
    tail: object
        pointer point to the tail of dllist
    """

    def __init__(self, capacity):
        """Initialize class variables

        Parameters
        ..........
        capacity: int
            The max size of the cache
        """

        self.cache_dict = dict()
        self.cache_size = self.check_size(capacity)
        self.filled_cache = 0
        self.head = None
        self.tail = None

    def check_size(self, capacity):
        if capacity <= 0:
            raise Exception("Cache size cannot be less or equal to 0")
        return capacity

    def get(self, key):
        """Retrieve item from provided key. Return -1 if nonexistent.

        Parameter:
        ..........
        key: int or str
            the key used to get corresponding item
        """
        if key in self.cache_dict:
            # if a node gets used, move this node to the end of queue
            value = self.cache_dict[key].value
            self.remove_from_list(key)
            self.add_to_tail(key, value)
            return value
        else:
            return -1

    def set(self, key, value):
        """Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item

        Parameter:
        ..........
        key: int or str
            the key used to set corresponding item
        value:
            the value will be stored
        """

        # if the cache is not at capacity, add the item to dictionary and
        # the DL list
        if key is None or value is None:
            raise Exception("Key or value cannot be None")
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
        """ Add one Node to the end of list
        Parameter:
        ..........
        key: int or str
            the key used to set corresponding item
        value:
            the value will be stored
        """
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


# Test Case 1, Invalid Input
try:
    one_cache = LRU_Cache(None)
except Exception:
    print("Invalid Cache Size")

try:
    one_cache = LRU_Cache(' ')
except Exception:
    print("Invalid Cache Size")

try:
    one_cache = LRU_Cache(0)
except Exception:
    print("Invalid Cache Size")

one_cache = LRU_Cache(3)
try:
    one_cache.set(1, None)
except Exception:
    print("Invalid key value pair")


# two_cache = LRU_Cache(' ')

# Exception, Cache size cannot be less or equal to 0


# Test Case 2
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)

try:
    print(our_cache.cache_dict[1])
except KeyError:
    print("(6,6) been added to the end, the key '1' has already beeen deleted")
print(our_cache.head.value)
# should be 2
print(our_cache.tail.value)
# should be 6
print(our_cache.get(1))
# should be -1
print(our_cache.get(2))
# should be 2
our_cache.set(7, 7)
# (3,3) should be deleted
print(our_cache.get(3))
# should be -1

# Test Case 3 large number

two_cache = LRU_Cache(3)
two_cache.set(1, 111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
print(two_cache.get(1))
