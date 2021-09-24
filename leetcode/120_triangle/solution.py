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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = list()
        cur_row = list()
        for i in range(len(triangle)-1, -1, -1):
            if i == len(triangle) - 1:
                prev_row = triangle[i]
            else:
                for idx, elem in enumerate(triangle[i]):
                    cur_row.append(elem + min(prev_row[idx], prev_row[idx+1]))
                prev_row = cur_row
                cur_row = list()
        return prev_row[0]


if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[[2],[3,4],[6,5,7],[4,1,8,3]]], 11),
        ([[[-10]]], -10),
    ]

    Tester.factory(test_cases, func=lambda input: sol.minimumTotal(*input)).run(unordered_output=False)
