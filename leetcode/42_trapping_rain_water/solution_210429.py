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
        # forward pass
        local_max = 0
        forward = list()
        for idx, num in enumerate(height):
            local_max = max(local_max, num)
            forward.append(local_max - num)

        # backward pass
        local_max = 0
        backward = list()
        for idx, num in enumerate(height[::-1]):
            local_max = max(local_max, num)
            backward.append(local_max - num)

        backward = backward[::-1]

        # print(f' forward: {forward}')
        # print(f'backward: {backward}')
        # print(f'    mins: {[min(forward[i], backward[i]) for i in range(len(height))]}')

        return sum([min(forward[i], backward[i]) for i in range(len(height))])


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
