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


tree = Tree("F")
tree.get_root().set_left_child(Node("B"))
tree.get_root().set_right_child(Node("G"))
tree.get_root().get_left_child().set_left_child(Node("A"))
tree.get_root().get_left_child().set_right_child(Node("D"))
tree.get_root().get_left_child().get_right_child().set_left_child(Node("C"))
tree.get_root().get_left_child().get_right_child().set_right_child(Node("E"))
tree.get_root().get_right_child().set_right_child(Node("I"))
tree.get_root().get_right_child().get_right_child().set_left_child(Node("H"))


# def in_order(tree):
#     visit_order = list()
#     if tree is None:
#         return []
#     root = tree.get_root()

#     if root.has_left_child():
#         in_order_traverse(root.get_left_child(), visit_order)
#     visit_order.append(root.get_value())
#     if root.has_right_child():
#         in_order_traverse(root.get_right_child(), visit_order)
#     return visit_order


# def in_order_traverse(node, visit_order):

#     if node.has_left_child():
#         in_order_traverse(node.get_left_child(), visit_order)
#     visit_order.append(node.get_value())
#     if node.has_right_child():
#         in_order_traverse(node.get_right_child(), visit_order)
#     return

def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child())

    traverse(root)
    return visit_order


print(in_order(tree))
