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
# ----------------------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        def map_alpha_to_num(char: str):
            return ord(char) - 97
        s_alpha = [0] * 26
        t_alpha = [0] * 26
        for idx in range(len(s)):
            s_alpha[map_alpha_to_num(s[idx])] += 1
            t_alpha[map_alpha_to_num(t[idx])] += 1
        return s_alpha == t_alpha


test_cases = [
    (["anagram", "nagaram"], True),
    (["rat", "car"], False),
]


if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.isAnagram(*input)).run(unordered_output=False)
