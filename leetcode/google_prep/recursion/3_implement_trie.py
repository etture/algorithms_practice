class Trie:
    class TrieNode:
        def __init__(self, char: str, is_root=False, is_word=False):
            self.is_root = is_root
            self.char = char
            self.children = dict()
            self.is_word = is_word

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root_node = self.TrieNode('', is_root=True)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root_node
        for idx, char in enumerate(word):
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                if idx == len(word) - 1:
                    cur_node.is_word = True
            else:
                if idx == len(word) - 1:
                    next_node = self.TrieNode(char, is_word=True)
                else:
                    next_node = self.TrieNode(char)
                cur_node.children[char] = next_node
                cur_node = next_node
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root_node
        for idx, char in enumerate(word):
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root_node
        for idx, char in enumerate(prefix):
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return len(cur_node.children) > 0 or cur_node.is_word


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    # print(trie.root_node.children)
    assert trie.search("apple") == True   # returns true
    assert trie.search("app") == False     # returns false
    assert trie.startsWith("app") == True # returns true
    trie.insert("app")   
    assert trie.search("app") == True     # returns true

    trie2 = Trie()
    trie2.insert('a')
    print(trie2.search('a'))
    print(trie2.startsWith('a'))