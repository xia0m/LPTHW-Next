class StackNode(object):
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):

    def __init__(self):
        self.top = None

    def push(self, obj):
        """Pushes a new value to the top of the stack"""
        if self.top is None:
            self.top = StackNode(obj, None)
            return
        temp = self.top
        self.top = StackNode(obj, None)
        self.top.next = temp

    def pop(self):
        """Pops the value that is currently on the top of the stack"""
        if self.top is None:
            return None
        result = self.top.value
        self.top = self.top.next
        return result

    def top(self):
        """Returns a *reference* to the first item, does not remove"""
        return self.top.value

    def count(self):
        """Counts the number of elements in the stack"""
        if self.top is None:
            return 0
        node = self.top
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack"""
        print(mark)
        node = self.top

        while node:
            print(node.value)
            node = node.next


a_stack = Stack()

a_stack.push('a')
a_stack.push('b')
print(a_stack.count())
print(a_stack.top)
print(a_stack.pop())
a_stack.dump()
