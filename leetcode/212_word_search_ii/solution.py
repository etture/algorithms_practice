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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0: return []
        if len(board[0]) == 0: return []

        words = sorted(words, key=lambda x: -len(x))
        print(f'words: {words}')

        trie_map = dict()
        for word in words:
            cur = trie_map
            for idx, char in enumerate(word):
                if char not in cur:
                    cur[char] = dict()
                cur = cur[char]
        print(trie_map)

        answer = set()

        def recurse(coord: tuple, sequence: List[str], visited: List[tuple]):
            print(f'recurse -> coord: {coord}, sequence: {sequence}, visited: {visited}')
            print(f'  trie_map: {trie_map}')
            entries = list()
            cur_entry = trie_map
            for idx, char in enumerate(sequence):
                if char not in cur_entry: return
                entries.append(cur_entry)
                cur_entry = cur_entry[char]
            # if len(cur_entry) == 0:
            joined_word = ''.join(sequence)
            if joined_word in words:
                answer.add(joined_word)
                for s in sequence[::-1]:
                    if len(entries[-1][s]) == 0:
                        del entries[-1][s]
                        entries.pop(-1)
                    else:
                        break
                if len(entries) == 0:
                    return

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
            for d in dirs:
                new_row = coord[0] + d[0]
                new_col = coord[1] + d[1]
                new_coord = (new_row, new_col)

                if new_coord not in visited \
                        and 0 <= new_row < len(board) \
                        and 0 <= new_col < len(board[0]) \
                        and board[new_row][new_col] in cur_entry:
                    recurse(new_coord, sequence + [board[new_row][new_col]], visited + [new_coord])


        for r_idx in range(len(board)):
            for c_idx in range(len(board[0])):
                if board[r_idx][c_idx] not in trie_map: continue
                recurse((r_idx, c_idx), [board[r_idx][c_idx]], [(r_idx, c_idx)])
        
        return list(answer)

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([
            [
                ["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]
            ],
            ["oath","pea","eat","rain"]
        ], ["eat","oath"]),
        ([
            [
                ["a","b"],
                ["c","d"]
            ],
            ["abcb"]
        ], []),
        ([
            [
                ["a","b"],
                ["c","d"]
            ],
            ["abdc"]
        ], ["abdc"]),
        ([
            [
                ["o","a","b","n"],
                ["o","t","a","e"],
                ["a","h","k","r"],
                ["a","f","l","v"]
            ],
            ["oa","oaa"]
        ], ["oa","oaa"]),
        ([
            [
                ["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]
            ],
            ["oath","pea","eat","rain","hklf", "hf"]
        ], ["oath","eat","hklf","hf"]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.findWords(*input)).run(unordered_output=True)
