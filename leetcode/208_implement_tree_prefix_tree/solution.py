# Basic imports --------------------------------------------
from __future__ import annotations                         
import sys                                                 
# 파이썬 기본 재귀 limit이 1000이라고 함 --> 10^6으로 manual하게 설정
sys.setrecursionlimit(10**6)
from os.path import dirname, abspath, basename, normpath   
root = abspath(__file__)                                   
while basename(normpath(root)) != 'algo_practice':           
    root = dirname(root)                                   
sys.path.append(root)                                      
from utils.Tester import Tester, Logger                    
logger = Logger(verbose=False)                             
import pprint
pp = pprint.PrettyPrinter()
# ----------------------------------------------------------

class Trie:

    class Node:
        def __init__(self, is_terminal=False):
            self.children = dict()
            self.is_terminal = is_terminal

        def insert(self, word: str) -> None:
            if len(word) == 0: return
            terminal = len(word) == 1
            if word[0] not in self.children:
                self.children[word[0]] = Trie.Node()
            if terminal:
                self.children[word[0]].is_terminal = True
            # print(f'  node insert -> children: {self.children}')
            self.children[word[0]].insert(word[1:])

        def __repr__(self):
            return f'<Node -> is_terminal: {self.is_terminal}, children: {self.children}>'


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Trie.Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.head.insert(word)
        # print(f'insert -> trie: {self.head.children}')
        print(self.head)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.head
        for char in word:
            # print(f'search -> word: {word}, char: {char}, cur_node.children: {cur_node.children}')
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.is_terminal
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.head
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Solution:
    def solve(self, commands: List[str], params: List[str]) -> List[bool]:
        answer = list()
        for idx, command in enumerate(commands):
            if idx == 0:
                trie = Trie()
                answer.append(None)
            else:
                param = params[idx][0]
                if command == "insert":
                    answer.append(trie.insert(param))
                elif command == "search":
                    answer.append(trie.search(param))
                elif command == "startsWith":
                    answer.append(trie.startsWith(param))
        return answer



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (
            [
                ["Trie", "insert", "search", "search", "startsWith", "insert", "search"], 
                [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
            ],
            [None, None, True, False, True, None, True]
        ),
        (
            [
                ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"],
                [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
            ],
            [None,None,None,None,None,None,None,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True]
        ),
    ]

    Tester.factory(test_cases, func=lambda input: sol.solve(*input)).run(unordered_output=False)
