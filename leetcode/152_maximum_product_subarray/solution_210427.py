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
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = [0] * len(nums)
        min_so_far = [0] * len(nums)
        for idx, num in enumerate(nums):
            if idx == 0:
                max_so_far[idx] = num
                min_so_far[idx] = num
            else:
                max_so_far[idx] = max(num, num * max_so_far[idx-1], num * min_so_far[idx-1])
                min_so_far[idx] = min(num, num * max_so_far[idx-1], num * min_so_far[idx-1])
        return max(max_so_far)
        

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[2,3,-2,4]], 6),
        ([[-2,0,-1]], 0),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maxProduct(*input)).run(unordered_output=False)
