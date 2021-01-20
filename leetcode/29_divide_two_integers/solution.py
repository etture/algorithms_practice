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
    def divide(self, dividend: int, divisor: int) -> int:
        # without using *, /, or %
        negative = False
        if dividend < 0:
            negative = not negative
            dividend = -dividend
        if divisor < 0:
            negative = not negative
            divisor = -divisor
        counter = 0
        while dividend > 0:
            dividend -= divisor
            if dividend >= 0:
                counter += 1
        return counter if not negative else -counter


test_cases = [
    ([10, 3], 3),
    ([7, 3], 2),
    ([7, -3], -2),
    ([0, 1], 0),
    ([1, 1], 1),
]

if __name__ == '__main__':
    sol = Solution()
    Tester.factory(test_cases, func=lambda input: sol.divide(*input)).run(unordered_output=False)
