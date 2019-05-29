import sys


class Node(object):

    def __init__(self, value, frequency):
        self.frequency = frequency
        self.value = value
        self.left = None
        self.right = None


def huffman_encoding(data):
    char_dict = count_char(data)
    freq_list = tuple_list(char_dict)
    build_huffman_tree(freq_list)
    huffman_tree = freq_list[0][1]

    for key in char_dict:
        char_dict[key] = get_binary_value(key, huffman_tree)

    encoded_data = ""

    for character in data:
        encoded_data += char_dict[character]

    return encoded_data, huffman_tree


def build_huffman_tree(freq_list):
    while(len(freq_list) > 1):
        leftValue = freq_list[0][1]
        leftFrequency = freq_list[0][0]
        rightValue = freq_list[1][1]
        rightFrequency = freq_list[1][0]
        totalFrequency = leftFrequency + rightFrequency
        if type(leftValue) is str:
            leftNode = Node(leftValue, leftFrequency)
        else:
            leftNode = leftValue
        if type(rightValue) is str:
            rightNode = Node(rightValue, rightFrequency)
        else:
            rightNode = rightValue
        tree = Node('*', totalFrequency)
        tree.left = leftNode
        tree.right = rightNode

        freq_list.append((totalFrequency, tree))
        del freq_list[:2]

        freq_list.sort(key=lambda x: x[0])


def get_binary_value(key, tree):
    binary_value = get_binary_value_helper(tree, key)
    return binary_value[::-1]


def get_binary_value_helper(tree, key):
    if tree is None:
        return None
    elif tree.value == key:
        return ""
    left_answer = get_binary_value_helper(tree.left, key)
    if left_answer is not None:
        left_answer += '0'
        return left_answer
    right_answer = get_binary_value_helper(tree.right, key)
    if right_answer is not None:
        right_answer += '1'
        return right_answer
    return None


def count_char(data):
    char_dict = dict()
    for character in data:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict


def tuple_list(char_dict):
    a_list = list()
    for key, value in char_dict.items():
        a_list.append((value, key))
    a_list.sort()

    return a_list

# DECODING


def huffman_decoding(data, tree):
    decoded_data = ""
    if tree is None:
        return ""
    node = tree
    for digit in data:
        if node.value == '*':
            if digit == '0':
                node = node.left
            elif digit == '1':
                node = node.right
        if node.value != '*':
            decoded_data += node.value
            node = tree
    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
