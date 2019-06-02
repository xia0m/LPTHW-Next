class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        head = self.root
        for letter in word:
            if letter not in head.children:
                head.children[letter] = TrieNode()
            head = head.children[letter]
        head.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        head = self.root
        for letter in word:
            if letter in head.children:
                head = head.children[letter]
        return head.is_word


word_list = ['apple', 'bear', 'goo', 'good',
             'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos',
              'a', 'app', 'goods', 'goose', 'zebra']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
