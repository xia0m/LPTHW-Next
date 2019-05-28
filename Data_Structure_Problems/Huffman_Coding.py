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
        # if len(freq_list) == 2:
        #     continue
        freq_list.sort(key=lambda x: x[0])
    # print(len(freq_list))


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


huffman_encoding("aabbbbbcccdeeeeeee")


def huffman_decoding(data, tree):
    pass


# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print("The size of the data is: {}\n".format(
#         sys.getsizeof(a_great_sentence)))
#     print("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print("The size of the encoded data is: {}\n".format(
#         sys.getsizeof(int(encoded_data, base=2))))
#     print("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print("The size of the decoded data is: {}\n".format(
#         sys.getsizeof(decoded_data)))
#     print("The content of the encoded data is: {}\n".format(decoded_data))
