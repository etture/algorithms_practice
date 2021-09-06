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
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        if len(needle) > len(haystack): return -1

        pointer = 0
        for idx, char in enumerate(haystack):
            if pointer >= len(needle): 
                return idx - len(needle)
            if char == needle[pointer]:
                pointer += 1
            else:
                pointer = 0

        if pointer >= len(needle):
            return len(haystack) - len(needle)
        else:
            return -1
        
            
if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (["hello", "ll"], 2),
        (["aaaaa", "bba"], -1),
        (["aaaaa", ""], 0),
        (["", ""], 0),
        (["mississippi", "issip"], 4),
    ]

    Tester.factory(test_cases, func=lambda input: sol.strStr(*input)).run(unordered_output=False)
