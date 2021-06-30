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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        while True:
            broken = False
            char_at_position = ""
            for idx, s in enumerate(strs):
                # print(f's: {s}, s[i]: {s[i]}, char_at_position: {char_at_position}')
                if i >= len(s):
                    broken = True
                    break
                if idx == 0:
                    char_at_position = s[i]
                else:
                    if s[i] != char_at_position:
                        broken = True
                        break
            if broken: break
            else: prefix += char_at_position
            i += 1
        return prefix



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([["flower","flow","flight"]], "fl"),
        ([["dog","racecar","car"]], ""),
        ([["abcdefghijkl", "abcdefg"]], "abcdefg"),
    ]

    Tester.factory(test_cases, func=lambda input: sol.longestCommonPrefix(*input)).run(unordered_output=False)
