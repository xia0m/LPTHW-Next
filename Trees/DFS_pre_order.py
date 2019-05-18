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


class Tree():
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


def pre_order(tree):
    visit_order = list()
    if tree is None:
        return []
    node = tree.get_root()
    print(node.get_value())
    visit_order.append(node.get_value())

    if node.has_left_child():
        pre_order_traverse(node.get_left_child(), visit_order)
    if node.has_right_child():
        pre_order_traverse(node.get_right_child(), visit_order)

    return visit_order


def pre_order_traverse(node, visit_order):
    visit_order.append(node.get_value())
    if node.has_left_child():
        pre_order_traverse(node.get_left_child(), visit_order)
    if node.has_right_child():
        pre_order_traverse(node.get_right_child(), visit_order)
    return


print(pre_order(tree))
# pre_order(tree)
