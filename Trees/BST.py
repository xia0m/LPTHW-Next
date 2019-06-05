from collections import deque


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


# node0 = Node("apple")
# node1 = Node("banana")
# node2 = Node("orange")

# print(f"has left child? {node0.has_left_child()}")
# print(f"has right child? {node0.has_right_child()}")

# print("adding left and right children")
# node0.set_left_child(node1)
# node0.set_right_child(node2)

# print(f"has left child? {node0.has_left_child()}")
# print(f"has right child? {node0.has_right_child()}")


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a for loop (try one or both ways)
    """

    def insert(self, new_value):
        if self.root is None:
            self.root = Node(new_value)
            return
        node = self.root
        while node:
            if new_value == node.get_value():
                return
            if new_value < node.get_value():
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(Node(new_value))
                    return
            if new_value > node.get_value():
                if node.has_right_child():
                    node = node.get_left_child()
                else:
                    node.set_right_child(Node(new_value))
                    return

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert_with_recursion(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        def insert_with_recursion_traverse(node):

            if value < node.get_value():
                if node.has_left_child():
                    insert_with_recursion_traverse(node.get_left_child())
                else:
                    node.set_left_child(Node(value))
            if value > node.get_value():
                if node.has_right_child():
                    insert_with_recursion_traverse(node.get_right_child())
                else:
                    node.set_right_child(Node(value))
            if node.get_value() == value:
                return

        insert_with_recursion_traverse(self.root)
    """
    search function
    """

    def search(self, value):
        if self.root is None:
            return False
        node = self.root
        while node:
            if value == node.get_value():
                return True
            elif value < node.get_value():
                node = node.get_left_child()
            else:
                node = node.get_right_child()
        return False

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


# tree = Tree()
# tree.insert_with_loop(5)
# tree.insert_with_loop(6)
# tree.insert_with_loop(4)
# tree.insert_with_loop(2)
# tree.insert_with_loop(5)  # insert duplicate
# print(tree)

# tree = Tree()
# tree.insert_with_recursion(5)
# tree.insert_with_recursion(6)
# tree.insert_with_recursion(4)
# tree.insert_with_recursion(2)
# tree.insert_with_recursion(5)  # insert duplicate
# print(tree)
tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
""")
print(tree)
