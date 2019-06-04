class Heap:
    def __init__(self, initial_size):
        # initialize arrays
        self.cbt = [None for _ in range(initial_size)]
        # denotes next index where new element should go
        self.next_index = 0

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        self.cbt[self.next_index] = data
        if self.next_index > 0:
            parent_index = (self.next_index-1)//2
            child_index = self.next_index
            while self.cbt[child_index] < self.cbt[parent_index]:
                temp = self.cbt[child_index]
                self.cbt[child_index] = self.cbt[parent_index]
                self.cbt[parent_index] = temp
                child_index = parent_index
                parent_index = (child_index-1)//2
                if parent_index < 0:
                    break
        self.next_index += 1


test = Heap(10)

test.insert(15)
test.insert(10)
test.insert(40)
test.insert(20)
test.insert(30)
test.insert(5)
print(test.cbt)
