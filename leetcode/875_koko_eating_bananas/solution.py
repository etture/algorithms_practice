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

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(k: int, hours: int) -> bool:
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total <= hours
        
        if h < len(piles): return -1
        if h == len(piles): return max(piles)

        left, right = 1, max(piles)
        min_k = right
        while left < right:
            middle = (left + right) // 2
            if is_possible(middle, h):
                min_k = middle
                right = middle
            else:
                left = middle + 1
        return min_k



if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[3,6,7,11], 4], 11),
        ([[3,6,7,11], 8], 4),
        ([[30,11,23,4,20], 5], 30),
        ([[30,11,23,4,20], 6], 23),
        ([[312884470], 312884469], 2),
    ]

    Tester.factory(test_cases, func=lambda input: sol.minEatingSpeed(*input)).run(unordered_output=False)
