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
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            longer = s
            shorter = t
        else:
            longer = t
            shorter = s

        if len(longer) - len(shorter) > 1: return False
        if len(longer) == len(shorter):
            diff_cnt = 0
            for i in range(len(longer)):
                if longer[i] != shorter[i]:
                    diff_cnt += 1
                if diff_cnt > 1:
                    return False
            return diff_cnt == 1
        else:
            i = 0
            diff_cnt = 0
            while i < len(shorter):
                if shorter[i] != longer[i+diff_cnt]:
                    diff_cnt += 1
                else:
                    i += 1
                if diff_cnt > 1:
                    return False
            return True


if __name__ == '__main__':

    sol = Solution()

    test_cases = [
        (["ab", "acb"], True),
        (["", ""], False),
        (["a", ""], True),
        (["", "A"], True),
        (["abcde", "bbcde"], True),
        (["abcde", "bbcae"], False),
    ]
    Tester.factory(test_cases, func=lambda input: sol.isOneEditDistance(*input)).run(unordered_output=False)
