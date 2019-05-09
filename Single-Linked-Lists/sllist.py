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

    def pop(self):
        """Removes the last item and returns it ."""

    def shift(self, obj):
        """Another name for push."""

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

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
