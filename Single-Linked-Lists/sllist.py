class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list"""
        if self.begin is None:
            self.begin = SingleLinkedListNode(obj, None)
            return
        node = self.begin
        while node.next:
            node = node.next
        node.next = SingleLinkedListNode(obj, None)

    def pop(self):
        """Removes the last item and returns it ."""
        if self.begin is None:
            return None
        if self.begin.next is None:
            result = self.begin.value
            self.begin = None
            return result
        node = self.begin
        while node.next.next:
            node = node.next
        result = node.next.value
        node.next = None
        return result

    def shift(self, obj):
        """Another name for push."""
        if self.begin is None:
            self.begin = SingleLinkedListNode(obj, None)
            return
        temp = self.begin
        self.begin = SingleLinkedListNode(obj, None)
        self.begin.next = temp

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin is None:
            return None
        result = self.begin.value
        self.begin = self.begin.next
        return result

    def remove(self, obj):
        """Finds a matching item and removes it from the list"""
        if self.begin is None:
            raise Exception("List is Empty")
        if self.begin.value == obj:
            self.begin = self.begin.next
            return 0
        node = self.begin
        index = 1
        while node.next:
            if node.next.value == obj:
                node.next = node.next.next
                return index
            node = node.next
            index += 1
        raise Exception("Item not found")

    def first(self):
        """Returns a *reference* to the first item, does not remove"""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove"""
        node = self.begin
        while node.next:
            node = node.next
        return node.value

    def count(self):
        """Counts the number of elements in the list."""
        if self.begin is None:
            return 0
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """Get the value at index."""
        if self.begin is None:
            return None
        if index+1 > self.count():
            return None
        count = 0
        node = self.begin
        while index > count and node.next:
            node = node.next
            count += 1
        return node.value

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        print(mark)
        print(self.to_list())

    def to_list(self):
        if self.begin is None:
            return []
        a_list = []
        node = self.begin
        while node:
            a_list.append(node.value)
            node = node.next
        return a_list
