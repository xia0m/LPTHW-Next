class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def is_in_list(self, value):
        if self.head is None:
            return False
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    new_list = LinkedList()
    node = llist_1.head
    while node:
        new_list.append(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if not llist_1.is_in_list(node.value):
            new_list.append(node.value)
        node = node.next
    return new_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    new_list = LinkedList()
    node = llist_1.head
    while node:
        if llist_2.is_in_list(node.value):
            new_list.append(node.value)
        node = node.next
    return new_list


# Test case 1


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# expected:3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 32 -> 9 -> 1 -> 11 -> 1
print(intersection(linked_list_1, linked_list_2))
# expected: 4 -> 6 -> 6 -> 4 -> 21
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# expected:3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1
print(intersection(linked_list_3, linked_list_4))
# expected: empty


# Test Case 3: Empty List

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# expected:1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1
print(intersection(linked_list_5, linked_list_6))
# expected:empty
