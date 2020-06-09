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
logger = Logger(verbose=True)                             
# ----------------------------------------------------------

class Solution:
    def findWords_bad(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0 or len(board) > 0 and len(board[0]) == 0 or len(words) == 0:
            return []
        
        height = len(board)
        width = len(board[0])
        
        letters_dict = dict()
        for word in words:
            for idx in range(len(word)):
                complete_word = False
                if idx == len(word) - 1:
                    complete_word = True
                letters_dict[word[:idx+1]] = complete_word

        found_words = set()

        def dfs(r_i: int, c_i: int, prior: str, path: List[tuple]):
            if 0 <= r_i < height and 0 <= c_i < width \
                    and (r_i, c_i) not in path:
                cur_char = board[r_i][c_i]
                appended = prior + cur_char
                if appended in letters_dict:
                    if letters_dict[appended] == True:
                        found_words.add(appended)
                    path.append((r_i, c_i))
                    dfs(r_i+1, c_i, appended, path)
                    dfs(r_i-1, c_i, appended, path)
                    dfs(r_i, c_i+1, appended, path)
                    dfs(r_i, c_i-1, appended, path)

        for r_idx, row in enumerate(board):
            for c_idx, elem in enumerate(row):
                if elem in letters_dict:
                    dfs(r_idx, c_idx, '', [])

        return sorted(found_words)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
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

        if len(board) == 0 or len(board) > 0 and len(board[0]) == 0:
            return []
        height = len(board)
        width = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)
        
        found_words = set()

        def backtrack(r_i: int, c_i: int, prior: str, past: List[tuple]):
            if 0<=r_i<height and 0<=c_i<width:
                if (r_i, c_i) not in past:
                    elem = board[r_i][c_i]
                    substr = prior + elem
                    print(f'r_i: {r_i}, c_i: {c_i}, prior: {prior}, elem: {elem}')
                    if trie.search(substr):
                        found_words.add(substr)
                    if trie.startsWith(substr):
                        past.append((r_i, c_i))
                        backtrack(r_i-1, c_i, substr, past)
                        backtrack(r_i+1, c_i, substr, past)
                        backtrack(r_i, c_i-1, substr, past)
                        backtrack(r_i, c_i+1, substr, past)

        for r_idx, row in enumerate(board):
            for c_idx, elem in enumerate(row):
                if trie.startsWith(elem):
                    backtrack(r_idx, c_idx, '', [])

        return sorted(list(found_words))


'''메인 실행 코드 -- DO NOT TOUCH BELOW THIS LINE'''
# 테스트 케이스
# Tuple[0]은 input, Tuple[1]은 나와야 하는 expected output

test_cases = [
    (
        [
            [
                ['o','a','a','n'],
                ['e','t','a','e'],
                ['i','h','k','r'],
                ['i','f','l','v']
            ],
            ["oath","pea","eat","rain"]
        ],
        ["eat","oath"]
    ),
    (
        [
            [
                ['a', 'a']
            ],
            ['a']
        ],
        ['a']
    ),
    (
        [
            [
                ['a', 'a']
            ],
            ['aaa']
        ],
        []
    ),
    # (
    #     [
    #         [
    #             ["b","a","a","b","a","b"],
    #             ["a","b","a","a","a","a"],
    #             ["a","b","a","a","a","b"],
    #             ["a","b","a","b","b","a"],
    #             ["a","a","b","b","a","b"],
    #             ["a","a","b","b","b","a"],
    #             ["a","a","b","a","a","b"]
    #         ],
    #         ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
    #     ],
    #     ["aabbbbabbaababaaaabababbaaba","abaabbbaaaaababbbaaaaabbbaab","ababaababaaabbabbaabbaabbaba"]
    # )
]


solution = Solution().findWords

if __name__ == '__main__':
    Tester.factory(
        test_cases,
        func=lambda input: solution(*input)
    ).run()
