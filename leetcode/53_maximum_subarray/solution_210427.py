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
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        local_max = [0] * len(nums)
        for idx, num in enumerate(nums):
            if idx == 0:
                local_max[idx] = num
            else:
                local_max[idx] = max(num, num + local_max[idx-1])
        return max(local_max)
        

if __name__ == '__main__':
    sol = Solution()

    test_cases = [
        ([[-2,1,-3,4,-1,2,1,-5,4]], 6),
        ([[1]], 1),
        ([[5,4,-1,7,8]], 23),
    ]

    Tester.factory(test_cases, func=lambda input: sol.maxSubArray(*input)).run(unordered_output=False)
