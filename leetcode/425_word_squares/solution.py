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
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if len(words) == 0: return []
        square_len = len(words[0])

        trie_map = dict()
        for word in words:
            for i in range(len(word)-1):
                prefix = word[:i+1]
                if prefix not in trie_map:
                    trie_map[prefix] = set()
                trie_map[prefix].add(word)
        print(trie_map)

        def recurse(level: int, partial: List[str]):
            if level >= square_len:
                return [partial]
            prefix = ''
            for i in range(level):
                prefix += partial[i][level]
            print(f'partial: {partial}, prefix: {prefix}')
            if prefix not in trie_map:
                return []
            words_with_prefix = [word for word in trie_map[prefix]]
            print(f'  words_with_prefix: {words_with_prefix}')
            if len(words_with_prefix) == 0:
                return []
            valid_squares = list()
            for w in words_with_prefix:
                valid_squares.extend(recurse(level + 1, partial + [w]))
            print(f'    valid_squares: {valid_squares}')
            return valid_squares
            

        answer = list()
        for w_idx, word in enumerate(words):
            answer.extend(recurse(1, [word]))
            print(f' ----> answer: {answer}')
        return answer
    

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([["area","lead","wall","lady","ball"]], [
            [
                "ball",
                "area",
                "lead",
                "lady"
            ],
            [
                "wall",
                "area",
                "lead",
                "lady"
            ]
        ]),
        ([["abat","baba","atan","atal"]], [
            [
                "baba",
                "abat",
                "baba",
                "atal"
            ],
            [
                "baba",
                "abat",
                "baba",
                "atan"
            ]
        ]),
        ([["momy","oooo","yoyo"]], [
            [
                "momy",
                "oooo",
                "momy",
                "yoyo"
            ],
            [
                "oooo",
                "oooo",
                "oooo",
                "oooo"
            ],
            [
                "yoyo",
                "oooo",
                "yoyo",
                "oooo"
            ]
        ]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.wordSquares(*input)).run(unordered_output=True)
