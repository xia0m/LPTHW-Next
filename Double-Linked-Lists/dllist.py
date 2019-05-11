class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.end = None

    def push(self, obj):
        """Appedns a new value on the end of the list."""
        if self.head is None:
            self.head = DoubleLinkedListNode(obj, None, None)
            self.end = self.head
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = DoubleLinkedListNode(obj, None, node)
        self.end = node.next

    def pop(self):
        """Removes the last item and return it"""
        if self.head is None or self.end is None:
            return None
        if self.head == self.end:
            result = self.head.value
            self.head = None
            self.end = None
            return result
        result = self.end.value
        temp = self.end.prev
        temp.next = None
        self.end = temp
        return result

    def shift(self, obj):
        """Actually just another name for push."""
        if self.head is None:
            self.head = DoubleLinkedListNode(obj, None, None)
            self.end = self.head
            return
        if self.head == self.end:
            self.head = DoubleLinkedListNode(obj, self.end, None)
            self.end.prev = self.head
            return
        temp = self.head.next
        self.head = DoubleLinkedListNode(obj, self.head, None)
        temp.prev = self.head

    def unshift(self):
        """Removes the first itme (from begin) and returns it"""
        if self.head is None:
            return None
        if self.head == self.end:
            result = self.head.value
            self.head = None
            self.end = None
            return result
        temp = self.head.next
        self.head = temp
        self.head.prev = None

    def detach_node(self, node):
        """It should take a node, and detach it from the list, 
        whether the node is at the front, end, or in the middle."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list"""

    def first(self):
        """Return a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove"""

    def count(self):
        """Counts the number of elements in the list"""

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of the list"""


dlist = DoubleLinkedList()
# dlist.push('a')
# dlist.push('b')
# dlist.push('c')
dlist.shift('d')
dlist.shift('z')
dlist.unshift()
# print(dlist.pop())
# print(dlist.pop())
print(dlist.head)
