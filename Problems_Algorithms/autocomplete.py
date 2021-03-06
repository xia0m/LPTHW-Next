# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point

        # The Trie itself containing the root node and insert/find functions
        suffix_list = list()

        def suffix_traverse(node, suf):
            if node:
                if node.is_word:
                    suffix_list.append(suf)
                for char in node.children:
                    suffix_traverse(node.children[char], suf+char)

            else:
                return
        suffix_traverse(self, '')

        return suffix_list


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return TrieNode()
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test Case 1 - Normal Input
print("Test case 1")
pre = MyTrie.find('a')
print(pre.suffixes())
# expcted ['nt', 'nthology', 'ntagonist', 'ntonym']
pre2 = MyTrie.find('f')
print(pre2.suffixes())
# expected ['un', 'unction', 'actory']
pre3 = MyTrie.find('tri')
print(pre3.suffixes())
# expected ['e', 'gger', 'gonometry', 'pod']

# Test Case 2 - Empty Input
print("Test Case 2")
pre4 = MyTrie.find('')
print(pre4.suffixes())
# expected
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

# Test Case 3 - large input
print("Test Case 3")
pre4 = MyTrie.find('eieisjiefsaerswefwefwef')
print(pre4.suffixes())
# expected []
