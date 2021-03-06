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
    def trap(self, height: List[int]) -> int:
        forward_max, backward_max = list(), list()
        forward_prev, backward_prev = 0, 0
        for h in height:
            if h > forward_prev:
                forward_prev = h
            forward_max.append(forward_prev)
        for h in height[::-1]:
            if h > backward_prev:
                backward_prev = h
            backward_max.append(backward_prev)
        backward_max = backward_max[::-1]

        # print(f'forward: {forward_max}')
        # print(f'backward: {backward_max}')

        minimums = [forward_max[x] if forward_max[x] < backward_max[x] else backward_max[x] for x in range(len(height))]
        # print(f'minimums: {minimums}')

        rainwater = [minimums[x] - height[x] for x in range(len(height))]
        return sum(rainwater)

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[0,1,0,2,1,0,1,3,2,1,2,1]], 6),
        ([[4,2,0,3,2,5]], 9),
        ([[1,2,3,2,1]], 0),
        ([[3,2,1,2,3]], 4),
        ([[3,2,1,1,3]], 5),
        ([[1,3,5,2,1,3,1,6,1,2]], 14),
    ]

    Tester.factory(test_cases, func=lambda input: sol.trap(*input)).run(unordered_output=False)
