class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        hash_code = 0
        current_coefficient = 1
        for i in key:
            hash_code += ord(i)*current_coefficient
            current_coefficient *= self.p
        return hash_code


h = HashMap()
print(h.get_bucket_index('abcd'))
