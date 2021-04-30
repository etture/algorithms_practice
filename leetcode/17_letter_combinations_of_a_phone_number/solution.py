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
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        temp_answer = list()
        for idx, digit in enumerate(digits):
            if idx == 0:
                temp_answer  = list(letter_map[digit])
            else:
                temp = temp_answer
                temp_answer = list()
                for combo in temp:
                    for char in letter_map[digit]:
                        temp_answer.append(combo + char)
        return temp_answer




if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["23"], ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ([""], []),
        (["2"], ["a","b","c"]),
    ]

    Tester.factory(test_cases, func=lambda input: sol.letterCombinations(*input)).run(unordered_output=True)
