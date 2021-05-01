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
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0: return 0

        memo = list()
        for _ in range(len(text2) + 1):
            memo.append([0] * (len(text1) + 1))

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # pp.pprint(memo)
                # print(f'i: {i}, j: {j}')
                candidates = [memo[j][i+1], memo[j+1][i], memo[j+1][i+1]]
                t1, t2 = text1[i], text2[j]
                max_surrounding = max(candidates) if len(candidates) > 0 else 0
                if t1 == t2:
                    memo[j][i] = memo[j+1][i+1] + 1
                else:
                    memo[j][i] = max_surrounding

        return memo[0][0]



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        (['abcde', 'ace'], 3),
        (['abc', 'abc'], 3),
        (['abc', 'def'], 0),
        (['abcde', 'deabc'], 3),
        (['abcde', 'dexyz'], 2),
        (['abcde', 'zabzz'], 2),
        (['abcdefghijklmnop', 'k'], 1),
        (['', ''], 0),
        (["bsbininm", "jmjkbkjkv"], 1),
    ]

    Tester.factory(test_cases, func=lambda input: sol.longestCommonSubsequence(*input)).run(unordered_output=False)
