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
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        normal_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        order_idx_dict = dict()
        for idx, char in enumerate(order):
            order_idx_dict[char] = normal_alphabet[idx]
        translated_words = list()
        for word in words:
            new_word = ''
            for char in word:
                new_word += order_idx_dict[char]
            translated_words.append(new_word)
        # print(translated_words)
        # print(sorted(translated_words))
        return translated_words == sorted(translated_words)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"], True),
        ([["word","world","row"], "worldabcefghijkmnpqstuvxyz"], False),
        ([["apple","app"], "abcdefghijklmnopqrstuvwxyz"], False),
    ]

    Tester.factory(test_cases, func=lambda input: sol.isAlienSorted(*input)).run(unordered_output=False)
