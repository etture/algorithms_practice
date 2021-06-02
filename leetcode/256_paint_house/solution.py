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
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1: return min(costs[0])
        recent_row = list()
        for idx in range(1, len(costs)):
            if idx == 1:
                recent_row = costs[idx-1]
            recent_row = [c + min(recent_row[:c_idx] + recent_row[c_idx+1:])  for c_idx, c in enumerate(costs[idx])]
        return min(recent_row)


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[17,2,17],[16,16,5],[14,3,19]]], 10),
        ([[[17,2,17],[16,16,5],[14,19,3]]], 21),
        ([[[7,6,2]]], 2),
    ]

    Tester.factory(test_cases, func=lambda input: sol.minCost(*input)).run(unordered_output=False)
