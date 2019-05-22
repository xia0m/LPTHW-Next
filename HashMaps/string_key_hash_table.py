"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.
Hash Value = (ASCII value of First Letter * 100 ) +
ASCII Value of Second Letter
"""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """TODO: Input a string that's stored in 
        the table."""
        hash_index = self.calculate_hash_value(string)
        self.table[hash_index] = string

    def lookup(self, string):
        """TODO: Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_index = self.calculate_hash_value(string)
        if self.table[hash_index]:
            return self.table[hash_index]
        else:
            return -1

    def calculate_hash_value(self, string):
        """TODO: Helper function to calulate a
        hash value from a string."""
        if len(string) < 2:
            raise Exception("Length is less than 2")
        hashCode = ord(string[0])*100 + ord(string[1])
        return hashCode


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
