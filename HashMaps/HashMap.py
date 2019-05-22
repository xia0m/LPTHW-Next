class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = Non


class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        new_node = LinkedListNode(key, value)
        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        hash_code = 0
        current_coefficient = 1
        num_bucket = len(self.bucket_array)
        for i in key:
            hash_code += ord(i)*current_coefficient
            hash_code = hash_code % num_bucket
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_bucket
        return hash_code % num_bucket

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_bucket = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_bucket)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)
                head = head.next


h = HashMap()
print(h.get_bucket_index('ace'))
