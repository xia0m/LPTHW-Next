import hashlib
import datetime


class Block:

    def __init__(self, data, previous_hash, index=0):
        self.index = index
        self.prev = None
        self.timestamp = self.get_utc_time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.index}{str(self.timestamp)}{self.data}{self.previous_hash}".encode(
            'utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_utc_time(self):
        return str(datetime.datetime.now()).split('.')[0]


class BlockChain:

    def __init__(self):
        self.end = None

    def add_block(self, data):
        if self.end is None:
            self.end = Block(data, 0, 0)
            return
        temp = self.end
        hash = self.end.hash
        prev_index = self.end.index
        self.end = Block(data, hash, prev_index+1)
        self.end.prev = temp

    def print_blockchain(self):
        if self.end is None:
            print("Current Block Chain is Empty")

        def traverse(block_chain):
            if block_chain is None:
                return
            traverse(block_chain.prev)
            print(f"""
    Index:{block_chain.index}
    Timestamp:{block_chain.timestamp}
    Data:{block_chain.data}
    SHA256 Hash:{block_chain.hash} <-
    Prev_hash:{block_chain.previous_hash}""")
        traverse(self.end)


bc = BlockChain()
bc.add_block('first')
bc.add_block('second')
bc.print_blockchain()
