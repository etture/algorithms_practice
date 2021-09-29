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
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        num_str = str(x)
        for i in range(len(num_str) // 2):
            if num_str[i] != num_str[len(num_str)-1-i]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([121], True),
        ([-121], False),
        ([10], False),
        ([-101], False),
    ]

    Tester.factory(test_cases, func=lambda input: sol.isPalindrome(*input)).run(unordered_output=False)
