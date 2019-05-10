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
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = DoubleLinkedListNode(obj, None, node)
        self.end = node.next

    def pop(self):
        """Removes the last item and return it"""

    def shift(self, obj):
        """Actually just another name for push."""

    def unshift(self):
        """Removes the first itme (from begin) and returns it"""

    def detach_node(self, node):
        """"""

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
dlist.push('a')
dlist.push('b')
print(dlist.end)
