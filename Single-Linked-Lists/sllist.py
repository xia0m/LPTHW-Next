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

    def remove(self, obj):
        """Finds a matching item and removes it from the list"""

    def first(self):
        """Returns a *reference* to the first item, does not remove"""

    def last(self):
        """Returns a reference to the last item, does not remove"""

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

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""

    def to_list(self):
        if self.begin is None:
            return []
        a_list = []
        node = self.begin
        while node:
            a_list.append(node.value)
            node = node.next
        return a_list
