import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode(
            'utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_GMT_time(self):
        return time.time()


class BlockChain:

    def __init__(self):
        pass

    def add_block(self, data):
        pass

    def print_blockchain(self):
        pass
